# Write a function that receives as a parameter a regex string, a text string and a whole number x,
# and returns those long-length x substrings that match the regular expression.
import re

def substrings(regex, text, x):
    words = re.findall('\w+', text)
    result = []
    for word in words:
        if len(word) == x and re.match(regex, word):
            result.append(word)
    return result

print(substrings("A+b*cc", " BACC AAc Abccc AbBcc AAAccc Abcs", 5))