# Write a function that receives a variable number of positional arguments and a variable number of keyword arguments 
# and will return the number of positional arguments whose values can be found among keyword arguments values.

def function(*args, **kwargs):

    list_kw = list(kwargs.values())
    list_p = args
    count=0
    for i in range(0,len(args)):
       for j in range(0, len(kwargs)):
          if list_p[i] == list_kw[j]:
            count+=1 
            break
    return count

print(function(1, 2, 3, 4, x=1, y=2, z=3, w=5))    
