from sylbreak import break_syllables
from collections import defaultdict
import json

def encode_input(input_text, vocab_dict):
    # Replace spaces with "<_>" before syllable breaking
    text_with_tokens = input_text.replace(" ", "<_>")

    # Break into syllables (ensuring "<_>" remains untouched)
    syllables_string = break_syllables(text_with_tokens)

    # Split by spaces, keeping "<_>" intact
    syllables_list = syllables_string.split(" ")

    # Initialize an empty list to store the encoded IDs
    encoded_ids = []
    i = 0
    while i < len(syllables_list):
        syllable = syllables_list[i]
        
        # Check if the current syllable is '<' and the next two are '_' and '>'
        if syllable == "<" and i + 2 < len(syllables_list) and syllables_list[i + 1] == "_" and syllables_list[i + 2] == ">":
            encoded_ids.append(vocab_dict["<_>"])  # Encode as the <_> token
            i += 3  # Skip over the next two syllables ('_' and '>') since they're part of <_>
        elif syllable in vocab_dict:
            encoded_ids.append(vocab_dict[syllable])  # Encode regular syllable
            i += 1
        else:
            encoded_ids.append(vocab_dict.get("<UNK>"))  # Handle unknown syllable
            i += 1

    return encoded_ids

def decode_ids(encoded_ids, vocab_dict):
    # Create a reverse mapping from IDs to words
    reverse_vocab_dict = {v: k for k, v in vocab_dict.items()}

    # Find the ID for "<_>" (space token) in the vocabulary
    space_id = vocab_dict.get("<_>")

    # Initialize a list to store the decoded words
    decoded_words = []

    # Iterate through each encoded ID and look up the corresponding word
    for encoded_id in encoded_ids:
        if encoded_id == space_id:
            # If the token is "<_>", insert a space instead
            decoded_words.append(" ")
        elif encoded_id in reverse_vocab_dict:
            # Append the corresponding word
            decoded_words.append(reverse_vocab_dict[encoded_id])
        else:
            # If the ID is not found, append an unknown token (e.g., "<UNK>")
            decoded_words.append("<UNK>")

    # Join the list into a string and return it
    return "".join(decoded_words)  # Use "" instead of " " to preserve spacing

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

# Step 1: Tokenize into syllables
syllables_string = break_syllables(corpus)
syllables_list = syllables_string.split(" ")
syllables_list.extend(["<END>", "<PAD>", "<UNK>", "<_>"])
print(len(syllables_list))

# Step 4: Run BPE until we reach the desired vocabulary size
vocab = set(syllables_list)  # Unique initial tokens
print(len(vocab))

token_to_id = {token: i for i, token in enumerate(sorted(vocab))}
with open("tokenizer-v2/vocabs.json", "w", encoding="utf-8") as f:
    json.dump(token_to_id, f)
# write_into_file(token_to_id)
# sentence = "ထိုအချက်ကို တွေ့အောင်ရှာတတ်လျှင် ဖြစ်သည်။"
# encoded = encode_input(sentence, token_to_id)
# print(encoded)
# decoded = decode_ids(encoded, token_to_id)
# print(token_to_id.get("<UNK>"))
# write_into_file(decoded)