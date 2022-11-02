import os

def function(path):
    dict={}
    dict["full_path"] = os.path.abspath(path)
    dict["file_size"] = os.path.getsize(path)        
    dict["file_extension"] = os.path.splitext(path)[1]
    dict["can_read"] = os.access(path, os.R_OK)
    dict["can_write"] = os.access(path, os.W_OK)
    print (dict)



function('text.txt')