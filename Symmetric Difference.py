a = input()
x = set(map(int, input().split()))

b = input()
y = set(map(int, input().split()))

dif = x.difference(y)
inter = y.difference(x)
merge = sorted(dif.union(inter))

for i in merge:
    print(i)

# union() = [1,2] U [1,2] = [1,2,1,2]
# intersection = [1,2] I [1,2,3] = [1,2]
# difference = [1,2] D [2,3] = [1]