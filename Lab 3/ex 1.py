# Write a function that receives as parameters two lists a and b and returns a list of sets containing: (a intersected with b, a reunited with b, a - b, b - a)

def opp(a,b):

  list=[]
  # A ∩ B
  list.append(set(a).intersection(b))  
  # A U B
  list.append(set(a).union(b))
  # A / B  
  list.append(set(a).difference(set(b)))
  # B / A 
  list.append(set(b).difference(set(a)))
  return list

a = [10, 20, 30, 40, 80]
b = [100, 30, 80, 40, 60]

print(opp(a,b))