
def process(**kwargs):
        fib = [0, 1]
        valid_numbers=[]
        for i in range(1000):
            fib.append(fib[i] + fib[i+1])

        valid_numbers = fib      
        if "filters" in kwargs.keys():
          for key in kwargs["filters"]: 
            valid_numbers = list(filter(key, valid_numbers))

        if "offset" in kwargs.keys():
            valid_numbers = valid_numbers[kwargs["offset"]:]

        if "limit" in kwargs.keys():
            valid_numbers = valid_numbers[:kwargs["limit"]]
    
        return valid_numbers  


def sum_digits(x):
    return sum(map(int, str(x)))

print(process(
    filters=[lambda item: item % 2 == 0, lambda item: item == 2 or 4 <= sum_digits(item) <= 20],
    limit=2,
    offset=2
   
))