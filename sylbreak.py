# -*- coding:utf-8 -*-

import re

def create_break_pattern():
    """Creates and returns the regular expression pattern for Myanmar syllable breaking."""
    my_consonant = r"က-အ"
    en_char = r"a-zA-Z0-9"
    other_char = r"ဣဤဥဦဧဩဪဿ၌၍၏၀-၉၊။!-/:-@[-`{-~\s"
    subscript_symbol = r'္'
    a_that = r'်'

    # Regular expression pattern for Myanmar syllable breaking
    return re.compile(
        r"((?<!" + subscript_symbol + r")[" + my_consonant + r"]"
        r"(?!["
        + a_that + subscript_symbol + r"])"
        + r"|[" + en_char + other_char + r"])"
    )

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

    return segmented_line

if __name__ == "__main__":
    myanmar_text = "မြန်မာစာပေ"
    segmented_text = break_syllables(myanmar_text)
    print(segmented_text)