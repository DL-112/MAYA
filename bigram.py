import nltk
from nltk import bigrams
from collections import Counter
import sylbreak

# Ensure you have the necessary NLTK resources
try:
    nltk.data.find('tokenizers/punkt_tab')
except LookupError:
    nltk.download('punkt_tab')

def clean_line(line):
    """Clean the line by removing unwanted characters and whitespace."""
    return sylbreak.break_syllables(line)

def build_bigram_model(file_path):
    """Build and return a bigram model from the given Myanmar book."""
    bigram_model = Counter()

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                cleaned_line = clean_line(line)
                if cleaned_line:  # Check if the line is not empty after cleaning
                    # Tokenize the line into words
                    tokens = nltk.word_tokenize(cleaned_line)
                    # Generate bigrams from the tokens
                    line_bigrams = bigrams(tokens)
                    # Update the bigram model
                    bigram_model.update(line_bigrams)

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

    return bigram_model

# def main():
#     input_file = 'book.txt'  # Replace with your Myanmar book file name
#     bigram_model = build_bigram_model(input_file)
#     if bigram_model:  # Only print if the model was built successfully
#         # Print the most common bigrams
#         print("Most Common Bigrams:")
#         for bigram, count in bigram_model.most_common(10):
#             print(f"{bigram}: {count}")

# if __name__ == "__main__":
#     main()