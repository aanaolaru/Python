import os

def function(path):
    
    l1=[f for f in os.listdir(path)
          if os.path.isfile(os.path.join(path, f))]         
    l2=[]      
    for x in l1:
        l2.append(os.path.abspath(x))
    return l2

print(function('C:\\Program Files\\Windows Media Player'))