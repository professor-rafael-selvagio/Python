import random

# Lista de opções
opcoes = ["Pedra", "Papel", "Tesoura"]

# Sorteio aleatório para o computador
computador = random.choice(opcoes)

# Entrada do jogador
print("Escolha uma opção:")
print("1 - Pedra")
print("2 - Papel")
print("3 - Tesoura")
escolha = input("Digite o número correspondente: ")

# Converter entrada para a escolha do jogador
match escolha:
    case "1":
        jogador = "Pedra"
    case "2":
        jogador = "Papel"
    case "3":
        jogador = "Tesoura"
    case _:
        print("Escolha inválida! Tente novamente.")
        exit()

# Exibe as escolhas
print(f"\nVocê escolheu: {jogador}")
print(f"O computador escolheu: {computador}")

# Determinar o vencedor
match (jogador, computador):
    case (jogador, computador) if jogador == computador:
        print("Empate!")
    case ("Pedra", "Tesoura") | ("Papel", "Pedra") | ("Tesoura", "Papel"):
        print("Você venceu!")
    case _:
        print("O computador venceu!")
