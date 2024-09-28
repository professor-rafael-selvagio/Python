idade = int(input('Informe sua idade:'))

if 1 < idade < 110:
    print('Valido')

    if idade < 18:
        print('Menor')
    else:
        print('Maior')

else:
    print('Nao Valido')