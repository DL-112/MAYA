def write_alphabets(output_file):
    alphabets = [chr(i) for i in range(65, 91)] + [chr(i) for i in range(97, 123)]  # A-Z and a-z
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(alphabets))  # Write alphabets line by line

# Example usage
write_alphabets('dictionary/eng-alphabets.txt')
