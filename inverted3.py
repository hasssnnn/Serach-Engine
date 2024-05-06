import os
from collections import defaultdict
import re
from urllib.parse import unquote

text_dir = '1'
inverted_index = defaultdict(list)

def tokenize(text):
    words = re.findall(r'\w+', text.lower())
    return words
#https://sicom/soccer/2024/05/02/inter-miami-dolphins-inspired-jersey-leak.txt,
#https://www.si.com/soccer/2024/05/02/inter-miami-dolphins-inspired-jersey-leak

def filename_to_url(filename):
    parts = filename.split('___')
    if len(parts) >= 3:
        domain = parts[1].replace('___', '.')  # Extract the domain and replace underscores with dots
        path = parts[2].replace('__', '/')  # Extract the path and replace underscores with slashes
        if path.endswith('.txt'):
            path = path[:-4]  # Remove the '.txt' extension from the path
        return f'https://{domain}{path}'
    else:
        print(f"Invalid filename format: {filename}")
        return None

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
        urls = [filename_to_url(filename) for filename in files]
        file.write(f"{word}: {', '.join(urls)}\n")

print(f"Inverted index saved to {output_file}")

# Example usage:
search_term = 'goal'
if search_term in inverted_index:
    matching_files = inverted_index[search_term]
    urls = [filename_to_url(filename) for filename in matching_files]
    print(f"Documents containing '{search_term}': {', '.join(urls)}")
else:
    print(f"'{search_term}' not found in any document.")
