n, m = map(int, input().split())
n, m = min(n, m), max(n, m)
p = n
n = n ** 2
m = m ** 2
f = m / n
win = p
for x in range(1,p + 1):
    win += int(((m - f * x ** 2)) ** 0.5) * 4 + 1
win += int(m ** 0.5) * 2
win += 1
print(win)