from itertools import combinations

n = input().split()
s = []

for i in sorted(n[0]):
    s.append(i.upper())

a = [sorted(list(combinations(s, int(i)))) for i in range(int(n[1]) + 1)]

del a[0]

for i in range(len(a)):
    for j in range(len(a[i])):
        print(''.join(a[i][j]))