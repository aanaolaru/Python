
import os
from collections import Counter

def takeSecond(elem):
  return elem[1]


def Dir(my_path):
  
  extensions=[]
  for root,d_names,f_names in os.walk(my_path):
    for f in f_names:
      extensions.append( f[f.rfind("."):]) 
      
  l=list(Counter(extensions).items())
  l.sort(key=takeSecond, reverse=True)
  return l


def File(my_path):
    fi = os.path.basename(my_path).split('/')[-1]
    f=open(fi, "r")
    return str(f.read())[-20:]


def function(my_path):
  if os.path.isdir(my_path):  
     print(Dir(my_path) ) 
  elif os.path.isfile(my_path):  
     print(File(my_path) ) 
  
#function('C:\\Program Files\\TeamViewer')
function('C:\\Users\\Alina\\Desktop\\Python\\Lab4\\fisier_ex3.txt')