import json

def extract_values(data):
    """Recursively extract values from a dictionary or list."""
    if isinstance(data, dict):
        values = []
        for value in data.values():
            values.extend(extract_values(value))
        return values
    elif isinstance(data, list):
        values = []
        for item in data:
            values.extend(extract_values(item))
        return values
    else:
        return [str(data)]

def json_to_txt(json_file, txt_file):
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    values = extract_values(data)
    
    with open(txt_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(values))

# Example usage
json_to_txt('dictionary/names.json', 'dictionary/names.txt')
