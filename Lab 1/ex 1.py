
def find_gcd(x, y):
    while(y):
        x, y = y, x % y
    return x

l=[]  
n = int(input("Enter number of elements : "))
for i in range(0, n):
    number = int(input())
    l.append(number)
 
num1 = l[0]
num2 = l[1]
gcd = find_gcd(num1, num2)
 
for i in range(2, len(l)):
    gcd = find_gcd(gcd, l[i])
     
print(gcd)