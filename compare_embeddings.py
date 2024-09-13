import json
import numpy as np
from scipy.spatial.distance import cosine, euclidean

# Function to load embeddings from a JSON file
def load_embeddings(file_path):
    with open(file_path, 'r') as f:
        embeddings = json.load(f)
    return embeddings

# Function to compute cosine distance between two vectors
def cosine_distance(vec1, vec2):
    return cosine(vec1, vec2)

# Function to compare embeddings from two files and find those with distances below the threshold
def compare_embeddings(file1, file2, threshold=0.1):
    embeddings1 = load_embeddings(file1)
    embeddings2 = load_embeddings(file2)

    for key1, data1 in embeddings1.items():
        print(f"Finding ops for abstract {key1}...")
        vec1 = data1["embedding"]

        for key2, data2 in embeddings2.items():
            vec2 = data2["embedding"]
            dist = cosine_distance(vec1, vec2)

            if dist < threshold:
                print(f"Distance between {key1} and {key2}: {dist:.4f}")
                print(f"Text 1: {data1['text']}")
                print(f"Text 2: {data2['text']}\n")

# Example usage
if __name__ == "__main__":
    file1 = 'paper_embeddings.json'  # First embeddings file
    file2 = 'ari_embeddings.json'  # Second embeddings file

    # Define your threshold for similarity. Lower values indicate more similarity.
    threshold = 0.45

    # Choose between "cosine" or "euclidean" for the distance metric
    print("Starting embeddings comparison...")
    compare_embeddings(file1, file2, threshold=threshold)
