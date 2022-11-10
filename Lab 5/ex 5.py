

def numbers_found(list):
    new_list = []
    for i in list:
      if (str(type(i)).split("'")[1] in ['float','int','long']):
        new_list.append(i)
    return new_list


print(numbers_found([1, "2", {"3": "a"}, {4, 5}, 5, 6, 3.0]))