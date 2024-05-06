import os

def reverse_filename(filename):
    # Remove the file extension (.txt) and replace special characters with URL format
    url = filename.replace('.txt', '').replace('___', '.').replace('__', '/').replace('_', ':')
    return url

# Directory containing text files with formatted filenames
input_directory = 'extracted_content_2'  # Change this to your directory path

# Iterate through files in the directory
for filename in os.listdir(input_directory):
    if filename.endswith('.txt'):  # Process only text files
        file_path = os.path.join(input_directory, filename)
        # Extract the formatted filename from the file name
        formatted_filename = filename[:-4]  # Remove the .txt extension
        # Convert the formatted filename back to its corresponding URL
        original_url = reverse_filename(formatted_filename)
        print(f"Original URL for {filename}: {original_url}")

        # You can write the URLs to a text file or process them as needed
        # Example: writing to a text file
        with open('converted_urls.txt', 'a') as outfile:
            outfile.write(original_url + '\n')
