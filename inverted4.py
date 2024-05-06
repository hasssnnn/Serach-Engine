import os
import re
from collections import defaultdict

# Specify the directory containing the files
output_dir = "3"

# Inverted index
index = defaultdict(set)

# Iterate over all files in the directory
for filename in os.listdir(output_dir):
    filepath = os.path.join(output_dir, filename)

    # Open each file
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

        # Tokenize the content
        words = re.findall(r'\b\w+\b', content)

        # Add the words to the inverted index
        for word in words:
            index[word.lower()].add(filename)

# Function to search the inverted index
def search(word):
    # Get the set of filenames containing the word
    filenames = index.get(word.lower(), set())
    # Convert filenames back to URLs
    urls = [filename.replace("__", ".").replace("_", "/").replace(".txt", "").replace("www", "https://www").replace("__", ".") for filename in filenames]

    return urls

# Test the search function
word = "sport"  # Replace with your search word
urls = search(word)
print(f"The word '{word}' is found in the following URLs:")
for url in urls:
    print(url)
