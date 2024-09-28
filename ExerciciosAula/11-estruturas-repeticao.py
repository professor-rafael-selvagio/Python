'''
Maneiras de utilizar o laço de repetição FOR
'''

frutas = ["maçã", "banana", "laranja"]
for fruta in frutas:
    print(fruta)


for i in range(5):  # Vai de 0 até 4 (não inclui o 5)
    print(i)


for i in range(2, 10, 2):  # Começa em 2, vai até 9, com passo de 2
    print(i)


palavra = "Python"
for letra in palavra:
    print(letra)


dicionario = {'nome': 'Alice', 'idade': 25}
for chave in dicionario:
    print(chave)


for chave, valor in dicionario.items():
    print(f"{chave}: {valor}")


frutas = ["maçã", "banana", "laranja"]
for indice, fruta in enumerate(frutas):
    print(f"Fruta {indice}: {fruta}")


nomes = ["Alice", "Bob", "Charlie"]
idades = [25, 30, 35]
for nome, idade in zip(nomes, idades):
    print(f"{nome} tem {idade} anos")


numeros = [1, 2, 3, 4, 5]
quadrados = [x**2 for x in numeros]
print(quadrados)  # Saída: [1, 4, 9, 16, 25]


for i in range(5):
    if i == 3:
        print("Interrompendo o laço com break")
        break
else:
    print("Esse código será executado se não houver break")


numeros = {1, 2, 3, 4, 5}
for numero in numeros:
    print(numero)


tupla = (10, 20, 30)
for item in tupla:
    print(item)


matriz = [[1, 2], [3, 4], [5, 6]]
for linha in matriz:
    for item in linha:
        print(item)
