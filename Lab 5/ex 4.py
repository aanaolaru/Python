
def func(*args, **kwargs):
    l=[]
    for i in args:
        # if i is a dictionary
        if isinstance(i, dict):
            # if i contains minimum 2 keys
            if len(i.keys())>=2:
              # if i has at least one string key with minimum 3 characters
                if any(isinstance(key, str) and len(key)>=3 for key in i.keys()):
                    l.append(i)
            
    for i in kwargs.values():
        if isinstance(i, dict):
            if len(i.keys())>=2:
                if any(isinstance(key, str) and len(key)>=3 for key in i.keys()):
                   l.append(i)
    return l



print(func( {1: 2, 3: 4, 5: 6}, 
 {'a': 5, 'b': 7, 'c': 'e'}, 
 {2: 3}, 
 [1, 2, 3],
 {'abc': 4, 'def': 5},
 3764,
 dictionar={'ab': 4, 'ac': 'abcde', 'fg': 'abc'},
 test={1: 1, 'test': True}))