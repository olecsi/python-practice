n = int(input())
count = 0
suma = 0
def main(n, count, suma, j):
    if j == 0:
        x = count + 1
        y = count + 2
        z = count + 3
    if j == 1:
        x = n + 1
        y = count + 2
        z = count + 3
    if j == 2:
        x = count + 1
        y = n + 2
        z = count + 3
    if j == 3:
        x = count + 1
        y = count + 2
        z = n + 3
    if x == n:
        suma += 1
    if y == n:
        suma += 1
    if z == n:
        suma += 1
    if x < n:
        suma = main(n, x, suma, 1)
    if y < n:
        suma = main(n, y, suma, 2)
    if z < n:
        suma = main(n, z, suma, 3)
    return suma
print(main(n, count, suma, 0))