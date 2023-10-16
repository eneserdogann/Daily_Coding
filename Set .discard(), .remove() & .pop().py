n = int(input())
s = set(map(int, input().split()))

order_size = int(input())
orders = []
for i in range(order_size):
    orders.append(input().split())

for i in range(order_size):
    if orders[i][0] == 'pop':
        s.pop()
    elif orders[i][0] == 'remove':
        s.remove(int(orders[i][1]))
    elif orders[i][0] == 'discard':
        s.discard(int(orders[i][1]))

print(sum(s))

"""remove(): Bu fonksiyon, belirtilen eleman kümede bulunmazsa bir KeyError istisnası (exception) fırlatır. 
Yani, eğer kaldırmaya çalıştığınız eleman kümede yoksa, kodunuz hata verir. Kısacası, 
bu fonksiyon elemanın kesinlikle küp içinde bulunması gerektiğini varsayar.

discard(): Bu fonksiyon, belirtilen eleman küme içinde bulunmasa bile herhangi bir hata fırlatmaz. 
Eğer eleman küpte mevcutsa kaldırır, yoksa sessizce devam eder. 
Yani, elemanın küpte olup olmadığını kontrol etmez ve hata vermez."""