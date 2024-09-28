def somar(n1, n2):
    return n1 + n2

def subtrair(n1, n2):
    return n1 - n2

def multiplicar(n1, n2):
    return n1 * n2

def dividir(n1, n2):
    if n2 == 0:
        return "Erro: Divisão por zero não permitida"
    return n1 / n2

def calculadora():
    while True:
        print("\nSelecione a operação:")
        print("1 - Somar")
        print("2 - Subtrair")
        print("3 - Multiplicar")
        print("4 - Dividir")
        print("5 - Sair")
        
        escolha = input("Digite o número da operação (1/2/3/4/5): ")
        
        if escolha == '5':
            print("Saindo da calculadora. Até mais!")
            break
        
        if escolha in ['1', '2', '3', '4']:
            n1 = float(input("Digite o primeiro número: "))
            n2 = float(input("Digite o segundo número: "))
            
            if escolha == '1':
                operacao = "Soma"
                resultado = somar(n1, n2)
            elif escolha == '2':
                operacao = "Subtração"
                resultado = subtrair(n1, n2)
            elif escolha == '3':
                operacao = "Multiplicação"
                resultado = multiplicar(n1, n2)
            elif escolha == '4':
                operacao = "Divisão"
                resultado = dividir(n1, n2)
            
            print(f"Operação: {operacao}")
            print(f"Resultado: {resultado}")
        else:
            print("Opção inválida. Tente novamente.")

# Chamar a calculadora
calculadora()
