import pygame
import random

# Inicializa o Pygame
pygame.init()

# Definição de cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Dimensões da tela
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Definição da velocidade de atualização
clock = pygame.time.Clock()

# Classe para o jogador (quadrado controlado pelo usuário)
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([50, 50])
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH // 2
        self.rect.bottom = SCREEN_HEIGHT - 10

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5

        # Limitar movimento às bordas da tela
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH

# Classe para os obstáculos que caem
class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([random.randint(20, 100), random.randint(20, 50)])
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randint(-100, -40)
        self.speed_y = random.randint(4, 8)

    def update(self):
        self.rect.y += self.speed_y
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
            self.rect.y = random.randint(-100, -40)
            self.speed_y = random.randint(4, 8)

# Função principal do jogo
def game():
    # Criação dos grupos de sprites
    all_sprites = pygame.sprite.Group()
    obstacles = pygame.sprite.Group()

    # Criação do jogador
    player = Player()
    all_sprites.add(player)

    # Criação dos obstáculos
    for _ in range(10):
        obstacle = Obstacle()
        all_sprites.add(obstacle)
        obstacles.add(obstacle)

    # Variáveis do jogo
    score = 0
    font = pygame.font.SysFont(None, 36)
    game_over = False

    # Loop principal do jogo
    while not game_over:
        # Eventos do jogo
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

        # Atualiza as sprites
        all_sprites.update()

        # Verifica colisões entre jogador e obstáculos
        if pygame.sprite.spritecollideany(player, obstacles):
            game_over = True

        # Atualiza a pontuação
        score += 1

        # Preenche a tela com fundo preto
        screen.fill(BLACK)

        # Desenha todas as sprites
        all_sprites.draw(screen)

        # Mostra a pontuação na tela
        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, [10, 10])

        # Atualiza a tela
        pygame.display.flip()

        # Define a velocidade do jogo
        clock.tick(60)

    # Mensagem de fim de jogo
    screen.fill(BLACK)
    game_over_text = font.render(f"Game Over! Final Score: {score}", True, WHITE)
    screen.blit(game_over_text, [SCREEN_WIDTH // 3, SCREEN_HEIGHT // 2])
    pygame.display.flip()

    # Espera antes de fechar
    pygame.time.wait(10000)
    pygame.quit()

if __name__ == "__main__":
    game()