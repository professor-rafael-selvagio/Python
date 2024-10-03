import pygame

class BlocoDestrutivel:
    def __init__(self, screen, tile_size, x, y):
        self.screen = screen
        self.tile_size = tile_size
        self.image = pygame.Surface((tile_size, tile_size))  # Usar uma superfície como exemplo
        self.image.fill((0, 255, 0))  # Cor verde para o bloco
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self):
        self.screen.blit(self.image, self.rect)
