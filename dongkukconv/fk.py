import json
import re

# Function to process data
def clean_json_data(data):
    cleaned_data = []
    for entry in data:
        h_field = entry["h"]
        # Remove content within square brackets
        h_cleaned = re.sub(r'\[.*?\]', '', h_field)
        # Check if special characters exist
        if re.search(r'[~!@#$%^&*()_+{}|:"<>?`\-=\[\]\\;\',./]', h_cleaned):
            # Remove special characters
            h_cleaned = re.sub(r'[~!@#$%^&*()_+{}|:"<>?`\-=\[\]\\;\',./]', '', h_cleaned)
        # Update the entry with cleaned 'h' field
        cleaned_entry = {**entry, "h": h_cleaned}
        cleaned_data.append(cleaned_entry)
    return cleaned_data

# Read from input.json
with open('D:\document\GitHub\yhhangul-tools\dongkukconv\input.json', 'r', encoding='utf-8') as infile:
    input_data = json.load(infile)

# Process the data
output_data = clean_json_data(input_data)

# Write to output.json
with open('D:\document\GitHub\yhhangul-tools\dongkukconv\output.json', 'w', encoding='utf-8') as outfile:
    json.dump(output_data, outfile, ensure_ascii=False, indent=4)

print("Processing complete. Check output.json for results.")
