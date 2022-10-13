# Find The greatest common divisor of multiple numbers read from the console.

def find_gcd(x, y):
    while(y):
        x, y = y, x % y
    return x

array=[]  
n = int(input("Enter number of elements : "))
for i in range(0, n):
    number = int(input())
    array.append(number)
 

gcd = find_gcd(array[0], array[1])
 
for i in range(2, len(array)):
    gcd = find_gcd(gcd, array[i])
     
print("GCD:", gcd)