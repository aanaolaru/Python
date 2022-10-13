# Write a function that counts how many words exists in a text. 
# A text is considered to be form out of words that are separated by only ONE space. For example: "I have Python exam" has 4 words.

def count_words(string):
    # remove the spaces from start and end
    string=string.strip()

    count=1
    for i in string:
        if i==" ":
            count+=1
    return count
 
string=input()
print(count_words(string))
