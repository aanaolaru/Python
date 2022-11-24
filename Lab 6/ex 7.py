# Verify using a regular expression whether a string is a valid CNP 
import re

def valid_cnp(cnp):
    if re.match("^[1-9]\d{2}(0[1-9]|1[0-2])(0[1-9]|[12]\d|3[01])(0[1-9]|[1-4]\d|5[0-2]|99)(00[1-9]|0[1-9]\d|[1-9]\d\d)\d$", cnp):
        return True
    return False
   
print(valid_cnp("5011221234567"))
print(valid_cnp("1234567890123"))