# Open the input file
import re

# Open the input file
with open('urls_2.txt', 'r') as f:
    lines = f.readlines()

# Define the pattern to match
pattern = re.compile(r'.*_-_-_-_-.*')

# Filter lines that do not contain the pattern
filtered_lines = [line for line in lines if not re.match(pattern, line)]

# Write the filtered lines back to the file
with open('pure_files_2.1.txt', 'w') as f:
    f.writelines(filtered_lines)

print("Lines containing '_-_-_-_-_' removed.")
