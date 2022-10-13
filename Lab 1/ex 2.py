# Write a script that calculates how many vowels are in a string.

def countvowels(string):
    num_vowels=0
    for ch in string:
        if ch in "aeiouAEIOU":
           num_vowels = num_vowels+1
    return num_vowels


string = input()
print(countvowels(string))