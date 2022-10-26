# Compare two dictionaries without using the operator "==" returning True or False. 
# (Attention, dictionaries must be recursively covered because they can contain other containers, such as dictionaries, lists, sets, etc.)

def dict(d1,d2):
    for i in d1.keys():
        if i in d2:
            if not (d1.get(i)==d2.get(i)):
                return False
        else:
            return False
    if len(d1)== len(d2):
        return True
    else:
        return False

print (dict({'number': 1, 'list': ['one', 'two']}, {'list': ['one', 'two'], 'number': 1}))
print (dict({'number': 2, 'list': ['one', 'two']}, {'number': 1, 'list': ['one', 'two'],}))