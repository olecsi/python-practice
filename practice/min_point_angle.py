import math
n = int(input())
res = 700
a1 = [list(map(int ,input().split()))for _ in range(n)]
for i in range(n):
    for h in range(n):
        if h == i:
            continue
        for g in range(n):
            if g == i or g == h:
                continue
            a = ((a1[h][0]- a1[g][0])**2 + (a1[h][1] - a1[g][1])**2)**0.5
            b = ((a1[h][0]- a1[i][0])**2 + (a1[h][1] - a1[i][1])**2)**0.5
            c = ((a1[i][0]- a1[g][0])**2 + (a1[i][1] - a1[g][1])**2)**0.5
            x = (b**2 + c**2 - a**2)/(2*b*c)
            x = max(-1, min(1, x))   #
            res = min(res, math.acos(x))
res = math.degrees(res)
print(f"{res:.4f}")
