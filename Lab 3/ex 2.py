# Write a function that receives a string as a parameter and returns a dictionary in which the keys are the characters in the character string 
# and the values are the number of occurrences of that character in the given text

def dict(string):

 freq = {}
  
 for i in string:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

 return freq

print(dict('Ana has apples.'))
