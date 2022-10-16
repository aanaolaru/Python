# Write a function that receives as parameter a list of numbers (integers) and will return a tuple with 2 elements. 
# The first element of the tuple will be the number of palindrome numbers found in the list and the second element will be the greatest palindrome number

def isPalindrome(n):
  copy=n
  pal=0
  while(n > 0):
    pal = pal*10 + n % 10
    n = n//10
  if(copy==pal):
    return True
  else:
    return False


def palindromeNumbers(list):
  count=0
  for n in list: 
        copy=n            
        pal = 0
        while copy > 0: 
            pal = pal*10 + copy % 10
            copy = copy//10
        if(n==pal):
            count+=1
  return count


def largestPalindrome(list, n):
   max = -1
   for i in range(0, n, 1):
      if (list[i] > max and isPalindrome(list[i])):
         max = list[i]
   return max



def function(list):
   return (palindromeNumbers(list), largestPalindrome(list, len(list)))
   


list = [10, 232, 5545455, 909090, 161]
print (function(list))   