import os
import argparse

def unique_extensions():
    
    parser = argparse.ArgumentParser()
    parser.add_argument("director", help="directorul in care se cauta extensiile")
    args = parser.parse_args()
    director = args.director

    l=[f for f in os.listdir(director)
          if os.path.isfile(os.path.join(director, f))] 

    l.sort(key=lambda f: os.path.splitext(f)[1])

    y=[]
    for x in l:
        y.append( x[x.rfind("."):])
    return list(set(y))

# python ex4.py 'C:\\Users\\Alina\\Desktop\\Python\\Lab4'  =>  ['.txt', '.py']