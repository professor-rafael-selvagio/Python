from random import randrange
from click import clear
clear()

def exibir_tabuleiro(tabuleiro):
    clear()
    print("+-------" * 3, "+", sep="")
    for linha in range(3):
        print("|       " * 3, "|", sep="")
        for coluna in range(3):
            print("|   " + str(tabuleiro[linha][coluna]) + "   ", end="")
        print("|")
        print("|       " * 3, "|", sep="")
        print("+-------" * 3, "+", sep="")

def realizar_jogada(tabuleiro):
    ok = False  # suposição falsa - precisamos dela para entrar no loop
    while not ok:
        jogada = input("Digite sua jogada: ")
        ok = len(jogada) == 1 and jogada >= '1' and jogada <= '9'  # a entrada do usuário é válida?
        if not ok:
            print("Jogada inválida – tente novamente!")  # não, não é - faça a entrada novamente
            continue
        jogada = int(jogada) - 1  # número de célula de 0 a 8
        linha = jogada // 3  # linha da célula
        coluna = jogada % 3  # coluna da célula
        sinal = tabuleiro[linha][coluna]  # verifica o quadrado selecionado
        ok = sinal not in ['O', 'X']
        if not ok:  # está ocupado - para a entrada novamente
            print("Campo já ocupado – tente novamente!")
            continue
    tabuleiro[linha][coluna] = 'O'  # coloca 'O' no quadrado selecionado

def fazer_lista_campos_livres(tabuleiro):
    livres = []
    for linha in range(3):  # iterar pelas linhas
        for coluna in range(3):  # iterar pelas colunas
            if tabuleiro[linha][coluna] not in ['O', 'X']:  # o campo está livre?
                livres.append((linha, coluna))  # sim, está - anexa uma nova tupla à lista
    return livres

def vitoria_para(tabuleiro, sinal):
    if sinal == "X":  # estamos procurando por X?
        quem = 'computador'  # sim - é o lado do computador
    elif sinal == "O":  # ... ou para O?
        quem = 'você'  # sim - é o nosso lado
    else:
        quem = None  # não devemos cair aqui!
    diagonal1 = diagonal2 = True  # para diagonais
    for rc in range(3):
        if tabuleiro[rc][0] == sinal and tabuleiro[rc][1] == sinal and tabuleiro[rc][2] == sinal:  # verifica a linha rc
            return quem
        if tabuleiro[0][rc] == sinal and tabuleiro[1][rc] == sinal and tabuleiro[2][rc] == sinal:  # verifica a coluna rc
            return quem
        if tabuleiro[rc][rc] != sinal:  # verifica a 1ª diagonal
            diagonal1 = False
        if tabuleiro[2 - rc][2 - rc] != sinal:  # verifica a segunda diagonal
            diagonal2 = False
    if diagonal1 or diagonal2:
        return quem
    return None

def realizar_jogada_computador(tabuleiro):
    livres = fazer_lista_campos_livres(tabuleiro)  # faz uma lista de campos livres
    quantidade = len(livres)
    if quantidade > 0:
        escolha = randrange(quantidade)
        linha, coluna = livres[escolha]
        tabuleiro[linha][coluna] = 'X'

tabuleiro = [[3 * j + i + 1 for i in range(3)] for j in range(3)]
tabuleiro[1][1] = 'X'  # coloca o primeiro 'X' no meio
livres = fazer_lista_campos_livres(tabuleiro)
vez_do_humano = True  # de quem é a vez?
while len(livres):
    exibir_tabuleiro(tabuleiro)
    if vez_do_humano:
        realizar_jogada(tabuleiro)
        vencedor = vitoria_para(tabuleiro, 'O')
    else:
        realizar_jogada_computador(tabuleiro)
        vencedor = vitoria_para(tabuleiro, 'X')
    if vencedor != None:
        break
    vez_do_humano = not vez_do_humano
    livres = fazer_lista_campos_livres(tabuleiro)

exibir_tabuleiro(tabuleiro)
if vencedor == 'você':
    print("Você venceu!")
elif vencedor == 'computador':
    print("Eu venci")
else:
    print("Empate!")
