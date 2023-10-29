import numpy

n = list(map(int, input().split()))
liste = []

for i in range(n[0]):
    liste.append(list(map(int, input().split())))

liste = numpy.array(liste)
print(max(numpy.min(liste, axis=1)))
