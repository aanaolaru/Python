# Write a function that validates if a number is a palindrome.

def palindrome(n):
  copy=n
  pal=0
  while(n > 0):
    pal = pal*10 + n % 10
    n = n//10

  if(copy==pal):
    print("The number is a palindrome!")
  else:
    print("The number isn't a palindrome!")


n=int(input("Enter number:"))
palindrome(n)
