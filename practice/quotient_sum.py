import math
n, u, d = map(int, input().split())
if d > u:
    print(0)
    exit()
if d == u:
    print(n)
    exit()
res = 0

k = u - d
i = 1
res += int(k/(d + i))
while int(k/(d + i)) != int(k/(d + i + 1)):
    i += 1
    if i > n:
        res += n 
        print(res)
        exit()
    res += int(k/(d + i)) 

x = int(k/(d + i))
if x == 0:
    res += n
    print(res)
    exit()
while i < n:
    l = math.ceil(k/x - d)
    if l > n:
        res += x *(n - i)
        res += n 
        print(res)
        exit()
    res += x * (l - i)
    i = l 
    x -= 1
    if x == 0:
        res += n 
        print(res)
        exit()
res += n
print(res)