# Read the content of the input file
input_file_path = 'pure_files_2.1.txt'
output_file_path = 'pure_urls_2.2.txt'

# List to store extracted URLs
urls = []

with open(input_file_path, 'r') as file:
    lines = file.readlines()
    for line in lines:
        # Extract URLs from lines starting with "Saving URL: "
        if line.startswith('Saving URL: '):
            url = line.replace('Saving URL: ', '').strip()
            urls.append(url)

# Save extracted URLs to the output file
with open(output_file_path, 'w') as file:
    for url in urls:
        file.write(f"{url}\n")

print(f"Extracted {len(urls)} URLs saved to '{output_file_path}'")
