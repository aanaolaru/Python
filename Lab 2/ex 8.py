# Write a function that receives a number x, default value equal to 1, a list of strings, and a boolean flag set to True.
# For each string, generate a list containing the characters that have the ASCII code divisible by x if the flag is set to True,
# otherwise it should contain characters that have the ASCII code not divisible by x


def function(x, list, flag):
    a=[]
    new_list=[]
    for i in range(0, len(list)):
        a=[]
        if flag == True:
            for j in range(0, len(list[i])):
               if ord(list[i][j]) % x == 0:
                 a.append(list[i][j])
        else:
             for j in range(0, len(list[i])):
               if ord(list[i][j]) % x != 0:
                 a.append(list[i][j]) 
                         
        new_list.append(a)
    return new_list             

print(function( 2, ["test", "hello", "lab002"], False))