import pygame
from campo import Campo
from player import Player  # Importar a classe Player
from bomba import Bomba  # Importar a classe Bomba


# Inicializando o pygame
pygame.init()

# Definindo as dimensões da tela
SCREEN_WIDTH = 13 * 40  # 13 colunas
SCREEN_HEIGHT = 11 * 40  # 11 linhas
TILE_SIZE = 40

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Bomberman Clone")

# Criar a instância da classe Campo
campo = Campo(screen, TILE_SIZE, 13, 11)

# Criar a instância da classe Player
player = Player(screen, TILE_SIZE, 0, 0)  # Começa na posição (0, 0)

# Criar a instância da classe Bomba
bomba_ativa = None

# Desenhar o campo e o jogador
campo.desenhar_campo()
campo.adicionar_blocos_destrutiveis()

def verificar_ocupacao(x, y, player, bomba_ativa, blocos_destrutiveis, blocos_indestrutiveis):
    # Verifica se a posição contém o jogador
    if player.rect.x == x and player.rect.y == y:
        return True  # Posição ocupada pelo jogador

    # Verifica se a posição contém uma bomba
    if bomba_ativa is not None and bomba_ativa.rect.x == x and bomba_ativa.rect.y == y:
        return True  # Posição ocupada pela bomba

    # Verifica se a posição contém um bloco destrutível
    for bloco in blocos_destrutiveis:
        bloco_rect = pygame.Rect(bloco[0] * TILE_SIZE, bloco[1] * TILE_SIZE, TILE_SIZE, TILE_SIZE)
        if bloco_rect.x == x and bloco_rect.y == y:
            return True  # Posição ocupada por um bloco destrutível

    # Verifica se a posição contém um bloco indestrutível
    for bloco in blocos_indestrutiveis:
        bloco_rect = pygame.Rect(bloco[0] * TILE_SIZE, bloco[1] * TILE_SIZE, TILE_SIZE, TILE_SIZE)
        if bloco_rect.x == x and bloco_rect.y == y:
            return True  # Posição ocupada por um bloco indestrutível

    return False  # Posição não ocupada

# Função principal do jogo
def game_loop():
    global bomba_ativa  # Declare bomba_ativa como global
    running = True
    bomba_ativa = None  # Inicializa a variável bomba_ativa fora do loop

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Verificar se o jogador pressionou a tecla de colocar bomba
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            if bomba_ativa is None:  # Se não houver bomba ativa
                # Cria uma nova bomba na posição do jogador
                bomba_ativa = Bomba(screen, TILE_SIZE, player.rect.x, player.rect.y)

        # Atualizar o jogador
        player.update(campo.get_blocos_destrutiveis(), campo.get_blocos_indestrutiveis())
        
        # Limpa a tela com um fundo branco
        screen.fill((255, 255, 255))  

        
        player.draw()  

        # Desenhar a bomba se estiver ativa
        if bomba_ativa is not None:
            bomba_ativa.draw(campo)  # Chama o método draw da bomba

        # Atualiza a tela
        pygame.display.update()

    pygame.quit()



if __name__ == '__main__':
    game_loop()
