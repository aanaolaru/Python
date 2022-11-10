
def dictionary(**kw):
    dict_list=[]
    dict={}
    for tup in list(kw.values())[0]:
        dict["sum"]= tup[0]+tup[1]
        dict["prod"]= tup[0]*tup[1]
        dict["pow"]= tup[0]**tup[1]
        dict_list.append(dict)
        dict={}
    print(dict_list)

print(dictionary(pairs = [(5, 2), (19, 1), (30, 6), (2, 2)] ))   