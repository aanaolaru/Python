#  Write a function that receives as a parameter a variable number of lists and a whole number x.
#  Return a list containing the items that appear exactly x times in the incoming lists

def function(*args):
    x=args[len(args)-1]
    args=args[:-1]   # scoate x 
    a= set().union(*args)
    b= [y for x in [*args] for y in x]
    c=[]
    for i in a:
        count=0
        for j in b:
            if i==j:
                count+=1   
        if count==x:
            c.append(i)  
    return c

print(function([1,2,3],[2,3,4],[4,5,6],[4,1,"test"],2)) 