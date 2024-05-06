import re

# Define the regular expression pattern to match valid lines
#pattern = re.compile(r'^[a-zA-Z0-9:/\.\?=:\(\)\s]+$')
pattern = re.compile(r'^[a-zA-Z0-9:/\.\?\-\s]+$')
# Input and output file paths
input_file_path = "Links/extracted_links.txt"
output_file_path = "cleaned2.txt"

# Read the input file and filter lines
with open(input_file_path, "r") as input_file:
    lines = input_file.readlines()
    filtered_lines = [line for line in lines if pattern.match(line.strip())]

# Write the filtered lines back to the output file
with open(output_file_path, "w") as output_file:
    filtered_lines = [line for line in filtered_lines if 'www' in line]
    output_file.writelines(filtered_lines)

print("Lines containing only valid characters kept successfully.")
