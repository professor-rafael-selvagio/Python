from click import clear
clear()

while True:
    n = int(input('Digite um número >= 0:'))

    if n >= 0:
        break


if n % 2 == 0:
    print('Par')
else:
    print('Impar')

