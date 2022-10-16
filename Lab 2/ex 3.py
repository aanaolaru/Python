# Write a function that receives as parameters two lists a and b and returns: (a intersected with b, a reunited with b, a - b, b - a)

def opp(a,b):

  # A ∩ B
  print(set(a).intersection(b))  
  # A U B
  print(set(a).union(b))
  # A / B  
  print(set(a).difference(set(b)))
  # B / A 
  print(set(b).difference(set(a)))


a = [10, 20, 30, 40, 80]
b = [100, 30, 80, 40, 60]
opp(a,b)
