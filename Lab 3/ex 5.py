# The validate_dict function that receives as a parameter a set of tuples ( that represents validation rules for a dictionary that has strings as keys and values) 
# and a dictionary. A rule is defined as follows: (key, "prefix", "middle", "suffix"). A value is considered valid if it starts with "prefix",
# "middle" is inside the value (not at the beginning or end) and ends with "suffix".
# The function will return True if the given dictionary matches all the rules, False otherwise.

import collections

def validate_dict(d, set):
  keys=[]
  for i,j in zip(d.keys(), d.values()):
   for index, rule in enumerate(list(set)):
        
        key = rule[0]
        prefix = rule[1]
        middle = rule[2]
        sufix = rule[3]
       
        if key == i:
            if not (j.startswith(prefix) and middle in j and j.endswith(sufix)):
                return False
            keys.append(key)
  if collections.Counter(keys) == collections.Counter(d.keys()):
    return True          
  else: return False

print(validate_dict({"key1": "come inside, it's too cold out", "key3": "this is not valid"}, {("key1", "", "inside", ""), ("key2", "start", "middle", "winter")}))