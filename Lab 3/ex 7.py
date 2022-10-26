# Write a function that receives a variable number of sets and returns a dictionary with the following operations from all sets two by two: 
# reunion, intersection, a-b, b-a. 
# The key will have the following form: "a op b", where a and b are two sets, and op is the applied operator: |, &, -. 

def function(*sets):
    dict={}
    index=0
    for s1 in sets :
        dict["{}|{}".format(s1,list(sets)[index+1])] =set(s1).union(list(sets)[index+1])
        dict["{}&{}".format(s1,list(sets)[index+1])] =set(s1).intersection(list(sets)[index+1])
        dict["{}-{}".format(s1,list(sets)[index+1])] =set(s1).difference(list(sets)[index+1])
        dict["{}-{}".format(list(sets)[index+1],s1)] =set(list(sets)[index+1]).difference(s1)
        index+=1
        if index==len(sets)-1:
            break
    return dict    

print(function({1,2}, {2, 3}, {4,1}))