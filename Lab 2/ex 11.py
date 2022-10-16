# Write a function that will order a list of string tuples based on the 3rd character of the 2nd element in the tuple. 
# Example: ('abc', 'bcd'), ('abc', 'zza')] ==> [('abc', 'zza'), ('abc', 'bcd')]

def Sort_Tuple(tup):
    
    for i in range(0, len(tup)): 
        for j in range(0, len(tup)-i-1):

              if tup[j][1][2] > tup[j + 1][1][2]:
                temp = tup[j]
                tup[j]= tup[j + 1]
                tup[j + 1]= temp
    return tup
 

tup =[('abc', 'bcd'), ('abc', 'zza'), ('abc', 'xyz'), ('abc', 'zzb')]  
print(Sort_Tuple(tup)) 