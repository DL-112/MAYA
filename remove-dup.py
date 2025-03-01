def remove_duplicates(input_files, output_file):
    unique_words = set()
    
    for file in input_files:
        with open(file, 'r', encoding='utf-8') as f:
            unique_words.update(f.read().splitlines())
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(sorted(unique_words)))

# Example usage
input_files = ['dictionary/dict-words.txt', 'dictionary/common-words.txt']
output_file = 'dictionary/unique_words.txt'
remove_duplicates(input_files, output_file)
