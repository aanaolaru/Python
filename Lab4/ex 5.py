import os

def function(target, to_search):
    l=[]
    if os.path.isfile(target):
        fd= open(target,'r')
        data = fd.read()
        if data.find(to_search):
            l.append(os.path.basename(target))
        fd.close()
        return l
    if os.path.isdir(target):
        for root,d_names,f_names in os.walk(target):
            for f in f_names:
                p_name = os.path.join(target,f)
                fd = open(p_name, 'r')
                data = fd.read()
                if data.find(to_search):
                    l.append(os.path.basename(f))
                fd.close()
        return l
    else:
        raise ValueError("target nu e fisier sau director")

print(function('C:\\Program Files\\Mozilla Firefox', 'A'))
