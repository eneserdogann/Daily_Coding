from itertools import product

x = input().split()
y = input().split()

x = [int(i) for i in x]
y = [int(j) for j in y]

a = list(product(x, y))

for i in a:
    print(i, end=' ')