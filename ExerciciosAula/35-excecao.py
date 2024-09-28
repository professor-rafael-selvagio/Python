try:
    idade = int(input('Digite sua idade em anos:'))
    meses = idade * 12
    print(f'Você tem {idade} em anos ou {meses} em meses')
except:
    print('Você digitou um texto no lugar da idade')
