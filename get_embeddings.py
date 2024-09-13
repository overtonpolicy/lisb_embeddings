import openai
import os
import json

# Set up your OpenAI API key
openai.api_key = "xxx"

# Function to get embeddings using OpenAI API
def get_embedding(text, model="text-embedding-3-small"):
    response = openai.embeddings.create(input=[text], model=model)
    return response.data[0].embedding

# Read lines from the input file and generate embeddings
def create_embeddings(input_file, output_file):
    embeddings = {}
    
    with open(input_file, 'r') as f:
        lines = f.readlines()

    for idx, line in enumerate(lines):
        line = line.strip()  # Clean the line from leading/trailing whitespace
        if line:  # Only process non-empty lines
            embedding = get_embedding(line)
            embeddings[f"line_{idx+1}"] = {
                "text": line,
                "embedding": embedding
            }
            print(f"Processed line {idx + 1}: {line}")

    # Save the embeddings to a JSON file
    with open(output_file, 'w') as f:
        json.dump(embeddings, f, indent=2)

    print(f"Embeddings saved to {output_file}")

# Example usage
if __name__ == "__main__":
    input_file = 'input.txt'    # File containing lines of text
    output_file = 'embeddings.json'  # Output file to store embeddings

    create_embeddings(input_file, output_file)
