import random as rnd
from click import clear
clear()


lista = [rnd.randint(1, 100) for i in range(10)]

print(f'Lista Original - {lista}')
lista.sort()
print(f'Lista Ordenada - {lista}')