# Write a functions that determine the most common letter in a string. 
# For example if the string is "an apple is not a tomato", then the most common character is "a" (4 times).
# Only letters (A-Z or a-z) are to be considered. Casing should not be considered "A" and "a" represent the same character.

def most_common_letter(string):
    string = string.lower()
    new_string = "".join(string.split())
    higher_count = 0
    return_character = ""

    for i in range(0, len(new_string)):
        count = 0
        length = len(new_string)
        j = 0
        character = new_string[i]
        while length > 0:
            if (character == new_string[j]):
                count += 1
            j += 1
            length -= 1    
            if (higher_count <= count):
                higher_count = count
                return_character = character
    return (return_character) 
 
string = input()
print (most_common_letter(string))