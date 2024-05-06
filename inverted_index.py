import os
from collections import defaultdict
import re

text_dir = 'extracted_content'
inverted_index = defaultdict(list)

# Function to tokenize text into words
def tokenize(text):
    words = re.findall(r'\w+', text.lower())
    return words

# Iterate through each text file in the text_dir
for filename in os.listdir(text_dir):
    if filename.endswith('.txt'):
        filepath = os.path.join(text_dir, filename)
        with open(filepath, 'r') as file:
            text = file.read()
            words = tokenize(text)
            # Update inverted index for each word
            for word in set(words):  # Using set to count occurrences only once per document
                inverted_index[word].append(filename)

# Save inverted index to a text file
output_file = 'inverted_index.txt'
with open(output_file, 'w') as file:
    for word, files in inverted_index.items():
        file.write(f"{word}: {', '.join(files)}\n")

print(f"Inverted index saved to {output_file}")
for filename in os.listdir(text_dir):
    if filename.endswith('.txt'):
        filepath = os.path.join(text_dir, filename)
        with open(filepath, 'r') as file:
            text = file.read()
            words = tokenize(text)
            # Update inverted index for each word
            for word in set(words):  # Using set to count occurrences only once per document
                inverted_index[word].append(filename)

# Example usage:
search_term = 'goal'
if search_term in inverted_index:
    matching_files = inverted_index[search_term]
    print(f"Documents containing '{search_term}': {matching_files}")
else:
    print(f"'{search_term}' not found in any document.")
