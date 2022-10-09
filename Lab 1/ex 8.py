
def  count_1Bits(n):
    count = 0
    while (n):
        count += n & 1
        n >>= 1
    return count
 
number = int(input())
print(count_1Bits(number))