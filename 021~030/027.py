# 027.py
n = 5
x = [9, 20, 28, 18, 11]
y = [30, 1, 21, 17, 28]

z = list(zip(x, y))

print(list(map(lambda a: bin(a[0] | a[1]).zfill(n)[2:].replace('1', '#').replace('0', ' '), z)))
