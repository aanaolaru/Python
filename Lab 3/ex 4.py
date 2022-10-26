def xml(tag, content, **kwargs):
    str1=""
    for i in kwargs.keys():
        str1 +=  str(i) + "=\"" + str(kwargs.get(i)) + "\""
    str2 = "<" + tag + " " + " " + str1 + ">" + content + " </" + tag + ">"
    return(str2)

print(xml("a", "Hello there", href =" http://python.org ", _class =" my-link ", id= " someid "))