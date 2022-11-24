# Write a function that extracts the words from a given text as a parameter. A word is defined as a sequence of alpha-numeric characters

import re

def extract_words(text):
    words = re.findall('[a-zA-Z1-9]+',text)
    return words

print(extract_words("Hello world!"))