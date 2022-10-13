# Write a script that receives two strings 
# and prints the number of occurrences of the first string in the second.

def count_occurrences(string1, string2):
    count=0
    for i in range(len(string2)-len(string1)+1):
        if string2[i:i+len(string1)] == string1 :      
            count+=1
    return count

string1 = input()
string2 = input()
print(count_occurrences(string1, string2))   