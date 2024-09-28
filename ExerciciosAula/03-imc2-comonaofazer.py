from click import clear
clear()

print(f'IMC: {round(float(input("Digite seu peso:")) / float(input("Digite altura:"))**2, 2)}')
