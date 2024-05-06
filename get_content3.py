import requests
from bs4 import BeautifulSoup
import os

# Specify the directory to save the files
output_dir = "3"

# Make sure the directory exists
os.makedirs(output_dir, exist_ok=True)

# Open the file and read the URLs
with open('cleaned2.txt', 'r') as f:
    urls = [line.strip() for line in f]

for url in urls:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Create a filename by replacing special characters in URL
    try:
        response = requests.get(url)
    except requests.exceptions.RequestException as e:
        print(f"Error occurred while requesting {url}: {e}")
        continue

    soup = BeautifulSoup(response.text, 'html.parser')

    # Create a filename by replacing special characters in URL
    filename = url.replace("https://", "").replace("/", "_").replace(".", "__") + ".txt"

    # Full path to the output file
    filepath = os.path.join(output_dir, filename)

    # Extract text from the webpage
    text = soup.get_text()

    # Save the text to a file
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(text)

    print(f"Saved content of {url} to {filepath}")
