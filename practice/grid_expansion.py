n, m = map(int, input().split())
a = [list(map(int, input().split()))for _ in range(n)]
count = 0
now = [a[0][0]]
place = [[0, 0]]

a[0][0] = 0
while m > 0 and now:
    place1 = []
    h = 0
    q = min(now)
    for i in range(len(now)):
        now[i] -= q
        if now[i] == 0:
            x = place[i][0]
            y = place[i][1]
            
            place1.append([x, y])

            h += 1
            if x != 0 and a[x-1][y] != 0:
                now.append(a[x - 1][y])
                place.append([x - 1, y])
                a[x - 1][y] = 0
            if x != n - 1 and a[x + 1][y] != 0:
                now.append(a[x + 1][y])
                place.append([x + 1, y])
                a[x + 1][y] = 0
            if y != 0 and a[x][y - 1] != 0:
                
                now.append(a[x][y - 1])
                place.append([x, y - 1])
                a[x][y - 1] = 0
            if y != n -1 and a[x][y + 1] != 0:
                
                now.append(a[x][y + 1])
                place.append([x, y + 1])
                a[x][y + 1] = 0
            count += 1
    m -= q
    for g in range(h):
        place.remove(place1[g])
        now.remove(0)
    if m < 0:
        count -= h
print(count)