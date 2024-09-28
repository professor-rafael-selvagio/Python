idade = int(input('Informe sua idade:'))

if idade <= 0 or idade > 110:
    print('Invalido')
else:
    print('Valido')

    if idade < 18:
        print('Menor')
    else:
        print('Maior')
    