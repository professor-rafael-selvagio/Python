from click import clear
clear()

lista = []

for i in range(5):
    lista.append([])
    for j in range(5):
        lista[i].append(j)

print(lista)