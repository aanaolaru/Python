# Write a function that will receive a list of words as parameter and will return a list of lists of words, grouped by rhyme. 
# Two words rhyme if both of them end with the same 2 letters

def get_by_rhyme(list):
    lst=[]
    new_list=[]

    
    while(list):
        new_list.append(list[0])
        list.pop(0)
        for i in range(0,len(list)):
       
          if new_list[0][len(new_list[0])-1] == list[i][len(list[i])-1] and new_list[0][len(new_list[0])-2] == list[i][len(list[i])-2]: 
             new_list.append(list[i])
             list[i]='NULL'
              
        lst.append(new_list)
        new_list=[]

    a=[]
    for i in lst:
      if i != ['NULL']:
        a.append(i)
        
    return a              

print(get_by_rhyme(['ana', 'banana', 'carte', 'arme', 'parte']))    