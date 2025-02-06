# Define the vocabulary
vocab = {
    "his": -1,
    "this": 0,
    "is": 1,
    "un": 3,
    "predict": 4,
    "able": 5,
    "dog": 6,
    "cat": 7,
    "fight": 8,
    "er": 9,
    "a": 10,
    "no": 11,
    "s": 12,
    "f": 13,
    "b": 14,
}

# Function to encode the sentence
def encode_sentence(sentence, vocab):
    # Convert the sentence to lowercase and split into words
    words = sentence.lower().split()
    
    # Encoded result
    encoded = []
    
    for word in words:
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

# Test the function
sentence = "fightersfightthisunpredictabledogs"
encoded_sentence = encode_sentence(sentence, vocab)
print("Encoded Sentence:", encoded_sentence)
