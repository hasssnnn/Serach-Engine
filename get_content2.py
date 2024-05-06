import os
import re
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

def fetch_web_page(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            text_content = soup.get_text()
            return text_content
        else:
            print(f"Error: Unable to fetch {url}. Status code: {response.status_code}")
            return None
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None

def get_filename(url):
    parsed_url = urlparse(url)
    domain = parsed_url.netloc.replace('.', '_')  # Replace dots in domain for filename compatibility
    path = parsed_url.path.replace('/', '_').replace('-', '_')  # Replace slashes and dashes in path for filename compatibility
    filename = domain + path + '.txt'
    return filename

# Example usage
# Read the URLs from a text file
with open('collected_links.txt', 'r') as file:
    urls = file.readlines()

output_directory = '1.1'
os.makedirs(output_directory, exist_ok=True)

# Process each URL
for url in urls:
    url = url.strip()
    filename = get_filename(url)
    file_path = os.path.join(output_directory, filename)
    
    web_page_content = fetch_web_page(url)
    if web_page_content:
        try:
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            with open(file_path, 'w') as file:
                file.write(web_page_content)
                print(f"Content of {url} saved to {file_path}")
        except FileNotFoundError as e:
            print(f"Error writing to {file_path}: {e}")
            continue
    else:
        print(f"Failed to fetch content from {url}")
