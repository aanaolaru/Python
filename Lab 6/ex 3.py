# Write a function that receives two parameters: a list of strings and a list of regular expressions. 
# The function will return a list of the strings that match on at least one regular expression from the list given as parameter
import re

def extract(text, regex_list):
    rez = []
    for exp in regex_list:
        rez += re.findall(exp,text)
    return set(rez)
    
print(extract("blabbalab bla bla ablaaab aabblbla, alab aaa",['a+.*a','.*la','bla']))