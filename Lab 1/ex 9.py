
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