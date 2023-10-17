stock_size = input()
stock = input().split()
stock = [int(i) for i in stock]
n = int(input())
cust = []
total_cost = 0

for i in range(n):
    cust.append(input().split())

for i in range(n):
    cust[i][1] = int(cust[i][1])
    cust[i][0] = int(cust[i][0])

for i in range(n):
    if cust[i][0] in stock:
        total_cost += cust[i][1]
        stock.remove(cust[i][0])

print(total_cost)