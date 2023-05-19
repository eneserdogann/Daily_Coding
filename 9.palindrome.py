x=121
x = str(x)
count=0
for index in range(0,int(len(x)/2+1)):
    if x[index] == x[len(x)-index-1]:
        count+=1
if count == int(len(x)/2+1):
    print('true')
else:
    print('false')