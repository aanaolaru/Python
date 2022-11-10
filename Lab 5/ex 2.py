
# function
def function(*args, **kwargs):
    return sum(kwargs.values())

print(function(1, 2, c=3, d=4))


# anonymous function
anon = lambda *args, **kwargs: sum(kwargs.values())
print(anon(1, 2, c=3, d=4))

