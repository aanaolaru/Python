
def first_number_in_text(string):
    first = 0 
    emp_str = ""
    for m in string:
      if m.isdigit():
        emp_str = emp_str + m
        first =1 
      elif first==1:
        break  
    return emp_str

text = input()       
print(first_number_in_text(text))


