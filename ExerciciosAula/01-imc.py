from click import clear
clear()

peso = 75
altura = 1.68

imc = peso / altura*altura

print(f'IMC: {imc:.2f}')
print(f'IMC: {round(imc, 2)}')
