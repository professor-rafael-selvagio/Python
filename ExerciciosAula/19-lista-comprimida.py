from click import clear
clear()

notas = [float(i) for i in input('Digite as notas:').split()]
media = sum(notas) / len(notas)

print(f'Para as notas {notas} sua média foi {media}')