import random
import sylbreak as sb
from collections import defaultdict

def load_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    text = sb.break_syllables(text)
    return text.split()

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
    words = load_text(file_path)
    bigrams = generate_bigrams(words)
    probabilities = calculate_probabilities(bigrams)
    return probabilities