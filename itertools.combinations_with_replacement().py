from itertools import combinations_with_replacement

n = input().split()
s = []

for i in sorted(n[0]):
    s.append(i.upper())

a = sorted(list(combinations_with_replacement(s, int(n[1]))))

for i in a:
    print(''.join(i))