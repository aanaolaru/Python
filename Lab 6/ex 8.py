# Write a function that recursively scrolls a directory and displays those files 
# whose name matches a regular expression given as a parameter or contains a string that matches the same expression.
# Files that satisfy both conditions will be prefixed with ">>"

import re
import os

def print_files(path, regex):
    files_in_dir = os.listdir(path) 
    for f in files_in_dir:
        if os.path.isfile(path + "/" + f):
            if re.match(regex, f) and re.search(regex, f):
                print(">>" + f) 
            elif re.match(regex, f) or re.search(regex, f): 
                print(f)
