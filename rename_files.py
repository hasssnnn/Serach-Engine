def filename_to_url(filename):
    parts = filename.split('___')
    if len(parts) >= 3:
        protocol_domain = parts[0].replace('https_', 'https://').replace('http_', 'http://')
        domain_parts = parts[1].split('__')
        if len(domain_parts) >= 2:
            domain = '.'.join(domain_parts[:-1])  # Join domain parts with dots
            if domain_parts[-1]:  # Check if there's a non-empty TLD
                domain += '.' + domain_parts[-1]
        else:
            domain = domain_parts[0]  # Only one domain part
        path_parts = parts[2:]
        path = '/'.join(part.replace('_', '/') for part in path_parts)  # Replace underscores with slashes in path parts
        if path.endswith('.txt'):
            path = path[:-4]  # Remove the '.txt' extension from the path
        return f'{protocol_domain}/{domain}/{path}'
    else:
        print(f"Invalid filename format: {filename}")
        return None

def fix_url(url_str):
    # Check if the URL already contains a dot after "www" and before the domain
    if "www/" in url_str:
        index_www = url_str.index("www")
        dot_index = url_str.find(".", index_www + 4)  # Look for dot after "www/"
        if dot_index == -1:
            # Add a dot after "www/" to fix the URL
            url_str = url_str[:index_www + 4] + "." + url_str[index_www + 4:]
    return url_str

# Example usage:
filename = "https_www___si___com___soccer___2024___05___02___inter-miami-dolphins-inspired-jersey-leak.txt"
original_url = filename_to_url(filename)
fixed_url = fix_url(original_url)
print("Modified URL from filename:", fixed_url)

# Example usage:
url = "https://www/si/com/soccer/2024/05/02/inter-miami-dolphins-inspired-jersey-leak"
fixed_url_from_url = fix_url(url)
print("Fixed URL from URL:", fixed_url_from_url)
