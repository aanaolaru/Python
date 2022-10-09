
def camel_to_snake(string):
    return ''.join(['_'+c.lower() if c.isupper() else c for c in string]).lstrip('_')

string = input()
print(camel_to_snake(string))