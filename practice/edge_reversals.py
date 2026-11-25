n, m, s, t = map(int, input().split())
if s == t:
    print(0)
    raise SystemExit

a = [list(map(int, input().split())) for i in range(m)]
graphs = {i:[] for i in range(n + 1)}

# Forward edges cost zero. Traversing an edge in reverse costs one.
for i in a:
    graphs[i[0]].append([i[1], 0])
    graphs[i[1]].append([i[0], 1])
visited = [False for i in range(n + 1)]
visited[s] = True
count = 0
sus = list()
def dfs(st):
    que = []
    que.extend(check(graphs[st]))
    while que:
        k = que.pop()
        if visited[k] == False:
            if k == t:
                print(count)
                exit()
            visited[k] = True
            que.extend(check(graphs[k]))
def check(l):
    global sus
    u = []
    for i in l:
        if i[1] == 1:
            if visited[i[0]] == False:
                sus.append(i[0])
        else:
            if visited[i[0]] == False:
                u.append(i[0])
    return u

dfs(s)


# Finish all zero-cost moves before expanding the next reversal layer.
while sus:
    count += 1
    h = 0
    for i in sus:
        if h == 0:
            sus = []
            h = 1
        if i == t:
            print(count)
            exit()
        if visited[i] == False:
            dfs(i)

print(-1)