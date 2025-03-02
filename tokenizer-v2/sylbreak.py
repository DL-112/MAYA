# -*- coding:utf-8 -*-

import re

def create_break_pattern():
    """Creates and returns the regular expression pattern for Myanmar syllable breaking."""
    my_consonant = r"က-အ၎"
    en_char = r"a-zA-Z0-9"
    other_char = r"ဣဤဥဦဧဩဪဿ၌၍၏၀-၉၊။!-/:-@[-`{-~\s“”—‘’…><"
    subscript_symbol = r'္'
    a_that = r'်'

    # Regular expression pattern for Myanmar syllable breaking
    return re.compile(
        r"((?<!" + subscript_symbol + r")[" + my_consonant + r"]"
        r"(?!["
        + a_that + subscript_symbol + r"])"
        + r"|[" + en_char + other_char + r"])"
    )

def process_string(input_string):
    # Function to check if the character is valid (contains '်', '့' and exactly one consonant)
    def is_valid_char(char):
        return '်' in char and '့' in char and len(char) == 3
    
    # Function to rearrange the Unicode order of specific marks
    def rearrange_unicode_order(word):
        splited = [c for c in word]
        splited[1], splited[2] = splited[2], splited[1]
        return ("").join(splited)

    # Process the string
    updated_string = []
    for word in input_string.split():
        if is_valid_char(word) and updated_string:
            updated_string[-1] += rearrange_unicode_order(word)  # Merge with the previous word
        else:
            updated_string.append(word)  # Otherwise, append as a new word

    return ' '.join(updated_string)

# main function to use sylbreak.py
def break_syllables(line):
    """Applies syllable breaking rules to a line."""
    break_pattern = create_break_pattern()
    separator = ' '
    line = re.sub(r'\s+', ' ', line.strip())
    segmented_line = break_pattern.sub(separator + r"\1", line)

    # Remove the leading delimiter if it exists
    if segmented_line.startswith(separator):
        segmented_line = segmented_line[len(separator):]

    # Replace delimiter+space+delimiter with a single space
    double_delimiter = separator + " " + separator
    segmented_line = segmented_line.replace(double_delimiter, " ")

    segmented_line = process_string(segmented_line)

    return segmented_line

if __name__ == "__main__":
    myanmar_text = "ကြည့်ပါ၎င်း"

    segmented_text = break_syllables(myanmar_text)
    def write_into_file(data, file_name="tokenizer-v2/screen.txt"):
        with open(file_name, "w", encoding="utf-8") as f:
            f.write(str(data))
    write_into_file(segmented_text)
    print(segmented_text)