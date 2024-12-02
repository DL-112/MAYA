import json
import numpy as np
from myparser import MyParser
import os

m = MyParser()

# Error threshold for classification
ERROR_THRESHOLD = 0.2

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "synapses.json")

# Load synapses from file
with open(file_path, "r", encoding="utf-8") as f:
    synapse = json.load(f)

synapse_0 = np.array(synapse["synapse0"])
synapse_1 = np.array(synapse["synapse1"])

words = synapse["words"]
classes = synapse["classes"]

def debug(msges, file_path):
    with open(file_path, "a", encoding="utf-8") as f:
        for msg in msges:
            f.write(f"{msg}, ")
        f.write("\n")

def debug2(msges, file_path):
    with open(file_path, "a", encoding="utf-8") as f:
        f.write(f"{msges}\n")

# Helper functions
def tokenize(sentence: str) -> list:
    """Break sentence into syllables and remove whitespaces."""
    return [item.strip() for item in m.syllable(sentence) if item.strip()]

def bow(sentence: str, words: list) -> np.ndarray:
    """Build a bag of words representation."""
    sentence_words = tokenize(sentence)
    bag = [1 if word in sentence_words else 0 for word in words]
    return np.array(bag)

# Classification
def think(sentence: str) -> np.ndarray:
    """Forward propagation to predict output."""
    x = bow(sentence, words)
    l0 = x
    l1 = sigmoid(np.dot(l0, synapse_0))
    l2 = sigmoid(np.dot(l1, synapse_1))
    return l2

def classify(sentence: str) -> list:
    """Classify a sentence into a category."""
    results = think(sentence)
    results_array = results.tolist()

    # Filter results above the error threshold
    trimmed_results = [(i, prob) for i, prob in enumerate(results_array) if prob > ERROR_THRESHOLD]

    # Sort results in descending order of probability
    trimmed_results.sort(key=lambda x: x[1], reverse=True)

    # Map results to class labels
    return_results = [(classes[i], prob) for i, prob in trimmed_results]

    # Default response if no results are above the threshold
    if not return_results:
        return_results.append(('မသိပါ', -1))

    print(f"{sentence} : {return_results}")
    debug(return_results, "output.txt")
    return return_results

# Sigmoid function
def sigmoid(x: np.ndarray) -> np.ndarray:
    return 1 / (1 + np.exp(-x))

# Example classifications
classify("နေကောင်းသွားပြီလား")
classify("ဒီကနေ့ဘာထူးလဲ")
classify("မနေ့ကကိစ္စ စိတ်မဆိုးနဲ့နော်")
classify("နားလည်ပေးလို့ အရမ်းကျေးဇူးတင်တယ်သိလား")
classify("သွားလိုက်ဦးမယ်၊ နောက်မှတွေ့ကြမယ်")
