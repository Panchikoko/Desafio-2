lista = [64, 34, 25, 12, 22, 11, 90]

n = len(lista)
i = 0

for i in range(n):
    j = 0
    for j in range(0, n-i-1):
        if lista[j] > lista[j+1]:
            print(lista)
            lista[j], lista[j+1] = lista[j+1], lista[j]

print("Lista ordenada:", lista)