# Write a function that extracts the words from a given text as a parameter. A word is defined as a sequence of alpha-numeric characters

import re

def extract_words(text):
    return re.findall('\w+', text)

print(extract_words("6R0T4A8% BF1 E #W@9 HI$MN*32V$5G P7Q"))

