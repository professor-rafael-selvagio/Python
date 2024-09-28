from click import clear
clear()

dia = int(input("Informe um número entre 1 e 7:"))

match dia:
    case 1: print("Domingo")
    case 2: print("Segunda")
    case 3: print("Terça")
    case 4: print("Quarta")
    case 5: print("Quinta")
    case 6: print("Sexta")
    case 7: print("Sábado")
    case 8 | 9 | 10: print("De 8 a 10")
    case _: print("Inválido")