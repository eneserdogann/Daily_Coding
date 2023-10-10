# Enter your code here. Read input from STDIN. Print output to STDOUT

r = input().split()
row = int(r[0])
col = int(r[1])
x = True
for i in range(1, int((row + 1) / 2)):
    for j in range(1, col + 1):
        if j > int((col - (6 * (i - 1) + 3)) / 2) and j <= int((col + (6 * (i - 1) + 3)) / 2):
            if j % 3 == 0:
                print('.|.', end='')
        else:
            print('-', end='')
    print('')

for i in range(1, col + 1):
    if x == True and i > (col - 7) / 2 and i < (col - 7) / 2 + 7:
        print('WELCOME', end='')
        x = False
    elif i <= (col - 7) / 2 or i >= (col - 7) / 2 + 8:
        print('-', end='')
print('')
# print('\n')
for i in range(1, int((row + 1) / 2)):
    for j in range(1, col + 1):
        if j > int(col - (col - (3 * i))) and j <= int(col - (3 * i)):
            if j % 3 == 0:
                print('.|.', end='')
        else:
            print('-', end='')
    print('')