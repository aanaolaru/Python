import os

def sort_extensions(director):
    l=[f for f in os.listdir(director)
          if os.path.isfile(os.path.join(director, f))] # lista cu fis din dir

    l.sort(key=lambda f: os.path.splitext(f)[1])

    y=[]
    for x in l:
        y.append( x[x.rfind("."):])
    return list(set(y))

print(sort_extensions('C:\\Program Files\\Windows Mail'))