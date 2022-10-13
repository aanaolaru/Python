#Write a script that converts a string of characters written in UpperCamelCase into lowercase_with_underscores.

def camel_to_snake(string):
    return ''.join(['_'+ ch.lower() if ch.isupper() else ch for ch in string]).lstrip('_')

string = input()
print(camel_to_snake(string))