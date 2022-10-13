# Write a function that counts how many bits with value 1 a number has. 
# For example for number 24, the binary format is 00011000, meaning 2 bits with value "1"

def  count_1Bits(n):
    binary=bin(n)
    bits = [bits_1 for bits_1 in binary[2:] if bits_1 == "1"]
    return len(bits)
 
number = int(input())
print(count_1Bits(number))