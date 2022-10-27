# Write a function that receives a single dict parameter named mapping. This dictionary always contains a string key "start". 
# Starting with the value of this key you must obtain a list of objects by iterating over mapping in the following way: 
# the value of the current key is the key for the next value, until you find a loop (a key that was visited before). 
# The function must return the list of objects obtained as previously described.

def loop(mapping):
    
    objects=[]
    position=0
    for x in mapping.values():
        for i in range(position+1, len(mapping.values())):
            if x == list(mapping.keys())[i]:
              objects.append(x)
        position+=1
    return set(objects)



print (loop({'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}))