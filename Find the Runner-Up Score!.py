x = 5
y = [2,3,6,6,5]

y.sort(reverse = True)

for i in range(len(y)-1):
    if y[i] > y[i+1]:
        print(y[i+1])
        break