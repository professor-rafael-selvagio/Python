import pygame
import os
from BlocoDestrutivel import BlocoDestrutivel  # Certifique-se de que a importação está correta

class Player:
    def __init__(self, screen, tile_size, x, y):
        self.screen = screen
        self.tile_size = tile_size
        self.image = pygame.image.load(os.path.join('Projetos/Pygame/Bomberman/assets', 'player.png'))
        self.image = pygame.transform.scale(self.image, (tile_size, tile_size))  # Redimensiona a imagem
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 1

    def update(self, blocos_destrutiveis, blocos_indestrutiveis):
        keys = pygame.key.get_pressed()
        original_x, original_y = self.rect.x, self.rect.y  # Armazena a posição original

        # Atualiza a posição com base nas teclas pressionadas
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:  # Tecla A também
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:  # Tecla D também
            self.rect.x += self.speed
        if keys[pygame.K_UP] or keys[pygame.K_w]:  # Tecla W também
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:  # Tecla S também
            self.rect.y += self.speed

        # Verifica se o jogador saiu da tela
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x > (self.screen.get_width() - self.tile_size):
            self.rect.x = self.screen.get_width() - self.tile_size
        if self.rect.y < 0:
            self.rect.y = 0
        if self.rect.y > (self.screen.get_height() - self.tile_size):
            self.rect.y = self.screen.get_height() - self.tile_size

        # Verifica colisões com blocos indestrutíveis
        for bloco in blocos_indestrutiveis:
            bloco_rect = pygame.Rect(bloco[0] * self.tile_size, bloco[1] * self.tile_size, self.tile_size, self.tile_size)
            if self.rect.colliderect(bloco_rect):
                self.rect.x, self.rect.y = original_x, original_y  # Reverte para a posição original
                break

        # Verifica colisões com blocos destrutíveis
        for bloco in blocos_destrutiveis:
            if isinstance(bloco, BlocoDestrutivel):  # Verifica se o objeto é um bloco destrutível
                bloco_rect = bloco.rect  # Usa o retângulo do objeto BlocoDestrutivel
                if self.rect.colliderect(bloco_rect):
                    self.rect.x, self.rect.y = original_x, original_y  # Reverte para a posição original
                    break

    def draw(self):
        self.screen.blit(self.image, self.rect)
