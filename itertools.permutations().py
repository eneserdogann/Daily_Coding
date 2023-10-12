from itertools import permutations

n = input().split()
s = []
for i in n[0]:
    s.append(i.upper())

a = sorted(list(permutations(s, int(n[1]))))

for i in a:
    print(''.join(i))