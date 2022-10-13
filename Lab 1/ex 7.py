# Write a function that extract a number from a text (for example if the text is "An apple is 123 USD", this function will return 123, 
# or if the text is "abc123abc" the function will extract 123). The function will extract only the first number that is found.

def first_number_in_text(string):
    first = 0 
    num = ""
    for ch in string:
      if ch.isdigit():
        num = num + ch
        first =1 
      elif first==1:
        break  
    return num

text = input()       
print(first_number_in_text(text))


