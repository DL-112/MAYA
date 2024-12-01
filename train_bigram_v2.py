import random
from word_breaker.word_segment_v5 import WordSegment
from collections import defaultdict

wordSegmenter = WordSegment()

def load_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    # text = sb.break_syllables(text)
    text = wordSegmenter.normalize_break(text, 'unicode', wordSegmenter.SegmentationMethod.sub_word_possibility)
    return text

def load_text_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # Process each line into a list of words, stripping any extra spaces
    word_lists = [line.strip().split(',') for line in lines]

    # Clean up any extra spaces around words and flatten the list
    word_lists = [word.strip() for word_list in word_lists for word in word_list]
    return word_lists

def generate_bigrams(words):
    bigrams = defaultdict(lambda: defaultdict(int))
    for i in range(len(words) - 1):
        bigrams[words[i]][words[i + 1]] += 1
    return bigrams

def calculate_probabilities(bigrams):
    probabilities = defaultdict(dict)
    for w1, w2_dict in bigrams.items():
        total_count = sum(w2_dict.values())
        for w2, count in w2_dict.items():
            probabilities[w1][w2] = count / total_count
    return probabilities

# Function to generate text
def generate_text(probabilities, start_word, num_words=50):
    current_word = start_word
    output = [current_word]
    for _ in range(num_words - 1):
        next_words = list(probabilities.get(current_word, {}).keys())
        if not next_words:
            break
        current_word = random.choices(next_words, weights=[probabilities[start_word][w] for w in next_words])[0]
        output.append(current_word)
        start_word = current_word
    return ' '.join(output)

# Main function to run the model
def train_bigram(file_path):
    # words = load_text(file_path)
    words = load_text_from_file("shwe_u_daung_S.txt")
    bigrams = generate_bigrams(words)
    probabilities = calculate_probabilities(bigrams)
    # print(probabilities)
    return probabilities