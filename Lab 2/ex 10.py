# Write a function that receives a variable number of lists and returns a list of tuples as follows: 
# the first tuple contains the first items in the lists, the second element contains the items on the position 2 in the lists, etc.

def zip_lists(*lists):
    max_size = len(max(lists, key = len))
    for ls in lists:
        while len(ls) < max_size:
            ls += [None]
    return list(zip(*lists))

print(zip_lists([1, 2, 3], [5, 6, 7, 8], ["a", "b", "c"]))