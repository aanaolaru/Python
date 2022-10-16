# Write a function to return a list of the first n numbers in the Fibonacci string

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-2)+fibonacci(n-1)

n=int(input())
for i in range(0, n):
    print(fibonacci(i), end=" ")

 