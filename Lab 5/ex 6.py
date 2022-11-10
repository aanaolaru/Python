def func(list):
    even = None
    odd = None
    tup_list=[]
    odd_count = 0
    for i in list:
        if i%2!=0:
            odd_count+=1

    for j in range(odd_count):
      for i in list:
            if i%2==0:
                even = i
                list.pop(list.index(i))
                break
      for i in list:
            if i%2!=0:
                odd = i
                list.pop(list.index(i))
                break
      tup_list.append((even, odd))

    return tup_list

print(func([1, 3, 5, 2, 8, 7, 4, 10, 9, 2]))