
# 8 a)
def multiply_by_two(x):
    return x * 2

def add_numbers(a, b):
    return a + b


def print_arguments(function):
    def wrapper(*args, **kwargs):
        print("Arguments are: ", args, ",", kwargs)
        return function(*args, **kwargs)
    return wrapper

augmented_multiply_by_two = print_arguments(multiply_by_two)
x = augmented_multiply_by_two(10) 
print(x)

augmented_add_numbers = print_arguments(add_numbers)
x = augmented_add_numbers(3, 4)
print(x)



# 8 b)
def multiply_by_three(x):
    return x * 3

def multiply_output(function):
    def wrapper(*args, **kwargs):
        return function(*args, **kwargs) * 2
    return wrapper

augmented_multiply_by_three = multiply_output(multiply_by_three)
x = augmented_multiply_by_three(10)
print(x)

# 8 c)
def add_numbers(a, b):
    return a + b

def augment_function(function, decorators):
    for decorator in decorators:
        function = decorator(function)
    return function
   

decorated_function = augment_function(add_numbers, [print_arguments, multiply_output]) 
x = decorated_function(3, 4) 
print(x)