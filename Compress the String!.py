n = input()
s = []
count = 1
for i in n:
    s.append(int(i))

for index, n_index in zip(s, s[1:]+[None]):
    if index == n_index:
        count += 1
    else:
        print(f'({count}, {index}) ', end='')
        count = 1