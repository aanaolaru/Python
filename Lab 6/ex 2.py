# Write a function that receives as a parameter a regex string, a text string and a whole number x,
# and returns those long-length x substrings that match the regular expression.
import re

def extract(regex, text, x):
    substrings = re.findall(regex,text)
    substrings = [w for w in substrings if len(w)==x]
    return substrings
print(extract("A+b*cc", " BACC AAc AbBcc AAAccc Abcs",5))