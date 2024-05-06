import os
import requests
from bs4 import BeautifulSoup
import urllib.parse

def fetch_web_page(url):
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the HTML content of the page using BeautifulSoup
            soup = BeautifulSoup(response.content, 'html.parser')
            # Extract the text content of the page (excluding HTML tags)
            text_content = soup.get_text()
            return text_content
        else:
            print(f"Error: Unable to fetch {url}. Status code: {response.status_code}")
            return None
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None

def format_filename(url):
    # Remove the protocol (http/https) and replace special characters with _
    formatted_url = url.replace('://', '_').replace('/', '__').replace('.', '___').replace(':','____')
    return formatted_url + '.txt'
#pattern = re.compile(r'^[a-zA-Z0-9:/\.\?\-\s]+$')

# Example usage
# Read the URLs from a text file
with open('cleaned1.txt', 'r') as file:
    urls = file.readlines()

# Create a directory to store all extracted content
output_directory = '1'
os.makedirs(output_directory, exist_ok=True)

# Process each URL
for url in urls:
    url = url.strip()  # Remove leading/trailing whitespace
    # Generate the filename based on the URL
    filename = format_filename(url)
    # Path to the file
    file_path = os.path.join(output_directory, filename)
    # Fetch the web page content
    web_page_content = fetch_web_page(url)
    if web_page_content:
        try:
            # Ensure the directory exists before writing the file
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            # Write the content to a text file
            with open(file_path, 'w') as file:
                file.write(web_page_content)
                print(f"Content of {url} saved to {file_path}")
        except FileNotFoundError as e:
            print(f"Error writing to {file_path}: {e}")
            continue  # Continue processing other URLs
    else:
        print(f"Failed to fetch content from {url}")
