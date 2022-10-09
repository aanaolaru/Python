def count_words(string):
    # Removing the spaces from start and end
    string=string.strip()

    count=1
    for i in string:
        if i==" ":
            count+=1
    return count
 
string=input()
print(count_words(string))
