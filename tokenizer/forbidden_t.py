from sylbreak import break_syllables
from collections import defaultdict

# Function to encode the sentence
def encode_sentence(sentence, vocab):
    syllables_string = break_syllables(sentence)
    syllables_list = syllables_string.split(" ")
    # Encoded result
    encoded = []
    
    for word in syllables_list:
        # Check if the word exists in the vocab directly
        if word in vocab:
            encoded.append(vocab[word])
        else:
            # Attempt to decompose the word into known vocab parts
            temp_encoded = []
            i = 0
            while i < len(word):
                matched = False
                # Try to match substrings of decreasing length
                for length in range(len(word), 0, -1):
                    part = word[i:i+length]
                    if part in vocab:
                        temp_encoded.append(vocab[part])
                        i += length  # Move the index past the matched part
                        matched = True
                        break
                if not matched:
                    print(f"Warning: Could not encode '{word}' at position {i}.")
                    i += 1  # Move one character forward in case no match found
            
            # Append the encoded parts if decomposition was successful
            if temp_encoded:
                encoded.extend(temp_encoded)
            else:
                print(f"Warning: Word '{word}' could not be encoded.")
    
    return encoded

def write_into_file(data, file_name="tokenizer-v2/screen.txt"):
    with open(file_name, "w", encoding="utf-8") as f:
        f.write(str(data))

# Sample Myanmar corpus
def read_and_combine_files(file_paths):
    combined_content = ""
    
    for file_path in file_paths:
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                combined_content += f.read() + "\n"  # Adding newline after each file's content
        except FileNotFoundError:
            print(f"Error: The file {file_path} was not found.")
        except Exception as e:
            print(f"An error occurred while reading {file_path}: {e}")
    
    return combined_content

corpus = read_and_combine_files(["dictionary/common-words.txt", "dictionary/dict-words.txt", "dictionary/stop-words.txt", "dictionary/special-tokens.txt"])

# Hyperparameters
VOCAB_SIZE = 5000  # Target vocabulary size

# Step 1: Tokenize into syllables
syllables_string = break_syllables(corpus)
syllables_list = syllables_string.split(" ")

# Step 2: Count pair frequencies
def count_pairs(syllables_list):
    pair_counts = defaultdict(int)
    for i in range(len(syllables_list) - 1):  # Iterate over adjacent pairs
        pair_counts[(syllables_list[i], syllables_list[i + 1])] += 1
    return pair_counts

# Step 3: Merge most frequent pair
def merge_pair(pair, syllables_list):
    merged = []
    i = 0
    while i < len(syllables_list):
        if i < len(syllables_list) - 1 and (syllables_list[i], syllables_list[i + 1]) == pair:
            merged.append("".join(pair))  # Merge the pair
            i += 2  # Skip the next element as it's merged
        else:
            merged.append(syllables_list[i])
            i += 1
    
    # Update the vocabulary by removing the individual syllables
    syllables_list[:] = merged
    return syllables_list

# Step 4: Run BPE until we reach the desired vocabulary size
vocab = set(syllables_list)  # Unique initial tokens
print(len(vocab))

token_to_id = {token: i for i, token in enumerate(vocab)}
write_into_file(token_to_id)
sentence = "ထိုအချက်ကိုတွေ့အောင်ရှာတတ်လျှင်ဖြစ်လေသည်။"
encoded = encode_sentence(sentence, token_to_id)
print(encoded)
exit(0)
i = 1
while len(vocab) < VOCAB_SIZE:
    pair_counts = count_pairs(syllables_list)
    if not pair_counts:
        break  # No more merges possible
    
    best_pair = max(pair_counts, key=pair_counts.get)  # Find most frequent pair
    syllables_list = merge_pair(best_pair, syllables_list)  # Merge the best pair

    # Update vocabulary with the merged pair
    new_token = "".join(best_pair)
    vocab.add(new_token)  # Add merged token to vocab
    # No need to discard individual syllables, we keep them for future merges
    if len(vocab) % 100 == 0: 
        print(len(vocab))
    i = i + 1

# Step 5: Assign token IDs
token_to_id = {token: i for i, token in enumerate(vocab)}

# Save vocabulary
write_into_file(token_to_id)

sentence = "ထိုအချက်ကိုတွေ့အောင်ရှာတတ်လျှင်ဖြစ်လေသည်။"
encoded = encode_sentence(sentence, vocab, token_to_id)
print(encoded)  # Output: [12, 34, 56] (example token IDs)
