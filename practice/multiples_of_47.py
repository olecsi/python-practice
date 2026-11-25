import math
a = int(input())
if a == 1:
    print(1)
    exit()
b = (10**(a - 1) - 1) // 47
c = ((10**a) - 1)// 47
print((c - b)%(10**9 + 7))