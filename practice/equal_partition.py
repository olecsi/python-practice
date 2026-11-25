n = int(input())
a = list(map(int, input().split()))
total = sum(a)
if total % 2 == 1:
    print(-1)
    exit()
total //= 2
dp = [-1] * (total + 1)


# dp[s] records the one-based index of the item that first made sum s reachable.
dp[0] = 0

for i, w in enumerate(a, start=1):
    # Sweep down so the current item cannot be used twice.
    for s in range(total, w - 1, -1):
        if dp[s] == -1 and dp[s - w] != -1:
            dp[s] = i
res = []
if dp[total] == -1:
    print(-1)
    exit()
q = [total]
while q:
    k = q.pop()
    r = dp[k] - 1
    res.append(r + 1)
    if k - a[r] == 0:
        break
    q.append(k - a[r])
print(len(res))
print(*res)