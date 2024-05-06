import os
from collections import defaultdict
import re

text_dir = '1'
inverted_index = defaultdict(list)

# Function to format filename to URL
def format_filename_to_url(filename):
    # Remove the file extension and replace special characters with their original form
    formatted_url = filename[:-4].replace('_____', '&').replace('______', '%').replace('_______', '?').replace('________', '(').replace('_________', ')').replace('__________', '=').replace('_______', '.').replace('____', ':').replace('___', '/').replace('__', '://')
    return formatted_url

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
output_file = 'inverted_index_urls.txt'
with open(output_file, 'w') as file:
    for word, files in inverted_index.items():
        urls = [format_filename_to_url(filename) for filename in files]
        file.write(f"{word}: {', '.join(urls)}\n")

print(f"Inverted index URLs saved to {output_file}")

# Example usage:
search_term = 'goal'
if search_term in inverted_index:
    matching_files = inverted_index[search_term]
    urls = [format_filename_to_url(filename) for filename in matching_files]
    print(f"Documents containing '{search_term}': {', '.join(urls)}")
else:
    print(f"'{search_term}' not found in any document.")
