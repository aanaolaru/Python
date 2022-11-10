
string = "Programming in Python is fun"

# Method 1
def func_vowels(string):
    vowels = []
    for i in string:
        if i in "aeiou":
            vowels.append(i)
    return vowels

print(func_vowels(string))


# Method 2 - using lambda and filter
vowels = list(filter(lambda x: x in "aeiou", string))
print(vowels)


# Method 3 - using lambda and list comprehension
vowels = lambda string:[x for x in string if x in "aeiou"]
print(vowels(string))


# Method 4 - using lambda, filter and list comprehension
vowels = list(filter(lambda x: x in "aeiou", [x for x in string]))
print(vowels)