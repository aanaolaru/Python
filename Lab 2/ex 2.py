from math import sqrt
# Write a function that receives a list of numbers and returns a list of the prime numbers found in it

def is_prime(n):
  flag = 0  
  if n > 1:  
    for i in range(2,int(n/2)+1):
       if n % i == 0:
         flag = 1
         break
    if flag==0:
      return "prime"
    else: return "not prime"
  else:  return "not prime"
 
def list_prime(list): 
	prime_list =[] 
	for i in list: 
		if (is_prime(i)=="prime"): 
			prime_list.append(i) 
	return prime_list 

print(list_prime([1, 9, 10, 2, 3, 5, 7, 12, 11, 13, 17, 19, 23]))     