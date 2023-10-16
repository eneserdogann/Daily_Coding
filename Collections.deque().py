from collections import deque

n = int(input())
a = []
b = [a.append(input().split()) for i in range(n)]

d = deque()

for i in a:
    if i[0] == 'append':
        d.append(i[1])
    elif i[0] == 'appendleft':
        d.appendleft(i[1])
    elif i[0] == 'pop':
        d.pop()
    elif i[0] == 'popleft':
        d.popleft()

for i in d:
    print(i, end=' ')