import requests
from bs4 import BeautifulSoup
import re

def remove_duplicates(l):
    unique_links = []
    for item in l:
        match = re.search("(?P<url>https?://[^\s]+)", item)
        if match is not None:
            url = match.group("url")
            if url not in unique_links:
                unique_links.append(url)
                for url in unique_links:
                    print(f"Saving URL: {url}")
    return unique_links

# Initialize variables
source_url = 'https://en.wikipedia.org/wiki/News' 
max_links = 100 # Maximum number of links to collect
output_file = 'collected_links2.txt'

# Fetch the initial page
try:
    source_code = requests.get(source_url)
    soup = BeautifulSoup(source_code.content, 'html.parser')
    all_links = [str(link.get('href')) for link in soup.find_all('a', href=True)]
except Exception as e:
    print(f"Error fetching {source_url}: {e}")
    exit(1)

# Remove duplicates and filter valid URLs
links = remove_duplicates(all_links)

# Collect additional links until the limit is reached or no more new links are found
while len(links) < max_links:
    new_links = []
    for link in links:
        try:
            source_code = requests.get(link)
            soup = BeautifulSoup(source_code.content, 'html.parser')
            extracted_links = [str(tag.get('href')) for tag in soup.find_all('a', href=True)]
            new_links.extend(extracted_links)
            for url in extracted_links:
                print(f"Saving URL: {url}")
        except Exception as e:
            print(f"Error fetching {link}: {e}")

    # Remove duplicates and filter valid URLs
    new_links = remove_duplicates(new_links)
    if not new_links or len(new_links) == len(links):  # No new links or no change in links
        break

    links.extend(new_links)  # Add new links to the existing list

# Write collected links to a text file
with open(output_file, 'w') as file:
    for url in links[:max_links]:  # Only save the first 10 links
        file.write(f"{url}\n")

print(f"Total unique links collected: {len(links)}")
print(f"Links saved to '{output_file}'")

# Fetch the initial page
try:
    source_code = requests.get(source_url)
    soup = BeautifulSoup(source_code.content, 'html.parser')
    all_links = [str(link.get('href')) for link in soup.find_all('a', href=True)]
except Exception as e:
    print(f"Error fetching {source_url}: {e}")
    exit(1)

# Remove duplicates and filter valid URLs
links = remove_duplicates(all_links)

# Collect additional links until the limit is reached or no more new links are found
while len(links) < max_links:
    new_links = []
    for link in links:
        try:
            source_code = requests.get(link)
            soup = BeautifulSoup(source_code.content, 'html.parser')
            extracted_links = [str(tag.get('href')) for tag in soup.find_all('a', href=True)]
            new_links.extend(extracted_links)
        except Exception as e:
            print(f"Error fetching {link}: {e}")

    # Remove duplicates and filter valid URLs
    new_links = remove_duplicates(new_links)
    if not new_links or len(new_links) == len(links):  # No new links or no change in links
        break

    links.extend(new_links)  # Add new links to the existing list

# Write collected links to a text file
with open(output_file, 'w') as file:
    for url in links[:max_links]:
        file.write(f"{url}\n")

print(f"Total unique links collected: {len(links)}")
print(f"Links saved to '{output_file}'")
