#  Write a function that receives as a parameter a list and returns a tuple (a, b), a representing the number of unique elements in the list,
#  and b representing the number of duplicate elements in the list (use sets to achieve this objective)

def tup(list):

   a = len(set(list)) # unique: apple, lemon, banana, orange, grape
   b = len(set([x for x in list if list.count(x) > 1])) # duplicates: apple, grape
   return a,b

list = ['apple', 'lemon', 'apple', 'banana', 'apple', 'apple', 'orange', 'grape', 'grape', 'apple']
print (tup(list))
