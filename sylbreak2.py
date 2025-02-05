def replace_or_remove_virama(text):
    """
    Replaces virama (Unicode 1039) with a-thet (Unicode 103A) or removes it if preceded by a-thet.
    Splits the string at replacement/removal points.
    """
    # Define Myanmar consonant range, virama, and a-thet
    myanmar_consonants = set(range(0x1000, 0x1022))  # Set of Unicode code points for Myanmar consonants
    virama = 0x1039  # Unicode code point for virama
    a_thet = chr(0x103A)  # Unicode character for a-thet

    result = []  # List to store the resulting syllables
    current_syllable = []  # List to build the current syllable
    i = 0
    n = len(text)

    while i < n:
        # Check if the current character is a Myanmar consonant and the next character is a virama
        if i + 1 < n and ord(text[i]) == virama:
            # Check if the character before the virama is an a-thet
            if i > 0 and ord(text[i - 1]) == 0x103A:
                i += 1  # Skip the consonant and virama
            else:
                # Replace the virama with a-thet
                current_syllable.append(a_thet)  # Add the a-thet
                i += 1  # Skip the consonant and virama

            # Split after the replacement/removal
            result.append(''.join(current_syllable))  # Add the current syllable to the result
            current_syllable = []  # Reset the current syllable
        else:
            # Append the current character to the current syllable
            current_syllable.append(text[i])
            i += 1

    # Add the last syllable if it exists
    if current_syllable:
        result.append(''.join(current_syllable))

    return result

# Example usage
if __name__ == "__main__":
    inputs = ["ကမ္ဘာ", "သက္ကတ", "အင်္ဂလိပ်", "ဗုဒ္ဓ", "သိပ္ပံ", "အက္ခရာ"]
    # inputs = ["အင်္ဂလိပ်"]
    result = [replace_or_remove_virama(input) for input in inputs]
    with open("output.txt", "w", encoding="utf-8") as f:
        f.write(str(result))
    print(result)