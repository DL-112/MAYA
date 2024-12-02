import numpy as np
import json
from typing import List, Tuple

# Load syllable breaker and ignore words
from myparser import MyParser
from ignore import ignore_words
from data import training_data

def debug(msges, file_path):
    with open(file_path, "a", encoding="utf-8") as f:
        for msg in msges:
            f.write(f"{msg}, ")
        f.write("\n")

def debug2(msges, file_path):
    with open(file_path, "a", encoding="utf-8") as f:
        f.write(f"{msges}\n")

m = MyParser()

print('------')
print(f"{len(training_data)} sentences in training data")
print('------')

# Tokenize function
def tokenize(sentence: str) -> List[str]:
    return [item.strip() for item in m.syllable(sentence) if item.strip()]

# Random number generator
def rand(rows: int, cols: int) -> np.ndarray:
    return 2 * np.random.random((rows, cols)) - 1

# Sigmoid and its derivative
def sigmoid(x: np.ndarray) -> np.ndarray:
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x: np.ndarray) -> np.ndarray:
    return x * (1 - x)

# Training Data Preparation
words = []
classes = []
documents = []

for pattern in training_data:
    w = tokenize(pattern['sentence'])
    words.extend(w)
    documents.append((w, pattern['class']))

    if pattern['class'] not in classes:
        classes.append(pattern['class'])

# Remove ignore words and duplicates
words = sorted(set(w for w in words if w not in ignore_words))
classes = sorted(set(classes))

print(f"{len(documents)} documents")
print(f"{len(classes)} classes")
print(f"{len(words)} unique words (syllables)")
print('------')

# Training data setup
training = []
output_empty = [0] * len(classes)
output = []

for doc in documents:
    bag = [1 if word in doc[0] else 0 for word in words]
    training.append(bag)

    output_row = output_empty[:]
    output_row[classes.index(doc[1])] = 1
    output.append(output_row)

training = np.array(training)
output = np.array(output)

# Training Model
def train(X: np.ndarray, y: np.ndarray, hidden_neurons: int, alpha: float, epochs: int, dropout: bool, dropout_percent: float):
    start_time = np.datetime64('now')

    print(f"Training with {hidden_neurons} neurons, alpha: {alpha}")
    print(f"Input matrix: {X.shape[0]}x{X.shape[1]}")
    print(f"Output matrix: 1x{len(classes)}")
    print('------')

    synapse_0 = rand(X.shape[1], hidden_neurons)
    synapse_1 = rand(hidden_neurons, len(classes))

    for j in range(epochs + 1):
        # Forward pass
        layer_0 = X
        layer_1 = sigmoid(np.dot(layer_0, synapse_0))
        
        if dropout:
            mask = np.random.binomial(1, 1 - dropout_percent, layer_1.shape)
            layer_1 *= mask
            layer_1 /= 1 - dropout_percent
        
        layer_2 = sigmoid(np.dot(layer_1, synapse_1))
        layer_2_error = y - layer_2

        if (j % 10000) == 0:
            mean_error = np.mean(np.abs(layer_2_error))
            print(f"Delta after {j} iterations: {mean_error}")
        
        # Backpropagation
        layer_2_delta = layer_2_error * sigmoid_derivative(layer_2)
        layer_1_error = layer_2_delta.dot(synapse_1.T)
        layer_1_delta = layer_1_error * sigmoid_derivative(layer_1)

        synapse_1 += layer_1.T.dot(layer_2_delta) * alpha
        synapse_0 += layer_0.T.dot(layer_1_delta) * alpha

    # Save synapses
    synapse = {
        "synapse0": synapse_0.tolist(),
        "synapse1": synapse_1.tolist(),
        "words": words,
        "classes": classes,
    }
    with open("synapses.json", "w", encoding="utf-8") as f:
        json.dump(synapse, f, indent=4)
    
    end_time = np.datetime64('now')
    training_time = (end_time - start_time).astype('timedelta64[s]').astype(int)
    if training_time > 60:
        print(f"Completed in: {training_time // 60} minutes {training_time % 60} seconds")
    else:
        print(f"Completed in: {training_time} seconds")
    print('------')

# Start training
train(training, output, hidden_neurons=20, alpha=0.01, epochs=100000, dropout=False, dropout_percent=0.2)
