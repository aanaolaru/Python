import os

def func(director, fisier):
    
    fi = os.path.basename(fisier).split('/')[-1]
    f=open(fi, "w")
   
    for dirpath,_,filenames in os.walk(director):
        for file in filenames:
         if str(file).startswith("A"):
             f.write(os.path.join(dirpath, file))
             f.write("\n")
           
    f.close()      

func('C:\\Program Files\\Mozilla Firefox', 'C:\\Users\\Alina\\Desktop\\Python\\Lab4\\fisier_ex2.txt')