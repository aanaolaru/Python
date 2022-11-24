# Write a function that, for a text given as a parameter, censures words that begin and end with vowels. 
# Censorship means replacing characters from odd positions with *
import re

def function(text):
    words = re.findall('\w+', text) 
    result = []
    for word in words:
        if re.match('[aeiouAEIOU]\w*[aeiouAEIOU]', word):
            result.append(word)
    censure = []
    for word in result:
        # replace characters from odd positions with * 
        censure.append(re.sub(r'(.)(.)', r'\1*', word))
    return censure

print(function("Ana are mere si pere"))


