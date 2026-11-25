def prefix_hesh_making(s, base, mod):
    n = len(s)

    h = [0]*(n + 1)
    p = [1] *(n + 1)

    for i in range(1, n + 1):
        h[i] = ((h[i -1] * base) + ord(s[i - 1]))% mod
        p[i] = (p[i - 1] * base)%mod

    return h, p

def get_hash(h, p, l, r, mod):
    # Remove the contribution preceding the half-open slice [l, r).
    return (h[r] - h[l] * p[r - l]) % mod

s = str(input())
n = len(s)

sr = s[::-1]
mod = 10**9 + 7
base = 10**9 - 1
h, p = prefix_hesh_making(s, base, mod)
hr, pr = prefix_hesh_making(sr, base, mod)


# Search from longest to shortest. Verify hash matches against the actual slices.
lpp = 0

for i in range(n, 0, -1):
    if get_hash(h, p, 0, i, mod) == get_hash(hr, pr, n - i, n, mod) and s[:i] == sr[n - i:]:
        lpp = i
        break

lco = 0

for i in range(n, 0, -1):
    if get_hash(h, p, n - i, n, mod) == get_hash(hr, pr, 0, i, mod) and s[n - i:] == sr[:i]:
        lco = i
        break
print(min(n - lco, n -lpp))