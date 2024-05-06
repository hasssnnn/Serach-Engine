import os
from collections import defaultdict
import re
from urllib.parse import unquote

text_dir = '1'
inverted_index = defaultdict(list)

def tokenize(text):
    words = re.findall(r'\w+', text.lower())
    return words

def filenames_to_urls(filenames):
    urls = [filename.replace("__", ".").replace("_", "/").replace(".txt", "").replace("www", "https://www").replace("__", ".") for filename in filenames]
    return urls

for filename in os.listdir(text_dir):
    if filename.endswith('.txt'):
        filepath = os.path.join(text_dir, filename)
        with open(filepath, 'r') as file:
            text = file.read()
            words = tokenize(text)
            for word in set(words):
                inverted_index[word].append(filename)

# Save inverted index to a text file
output_file = 'inverted_index2.txt'
with open(output_file, 'w') as file:
    for word, files in inverted_index.items():
        urls = ', '.join(filenames_to_urls(files))  # Join the URLs for each file
        file.write(f"{word}: {urls}\n")

print(f"Inverted index saved to {output_file}")

# Example usage:
search_term = 'goal'
if search_term in inverted_index:
    matching_files = inverted_index[search_term]
    urls = ', '.join(filenames_to_urls(matching_files))  # Join the URLs for matching files
    urls = ['https://' + url for url in urls]  # Add 'https://' before each URL
    print(f"Matching URLs for '{search_term}': {', '.join(urls)}")
else:
    print(f"'{search_term}' not found in any document.")
