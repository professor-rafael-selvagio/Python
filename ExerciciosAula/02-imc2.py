from click import clear
clear()

peso = float(input("Digite seu peso:"))
altura = float(input("Digite altura:"))

imc = peso / altura**2

print(f'IMC: {imc:.2f}')
print(f'IMC: {round(imc, 2)}')
