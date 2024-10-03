import pygame
import os
import time

class Bomba:
    def __init__(self, screen, tile_size, x, y):
        self.screen = screen
        self.tile_size = tile_size
        self.image = pygame.image.load(os.path.join('Projetos/Pygame/Bomberman/assets', 'bomb.png'))
        self.image = pygame.transform.scale(self.image, (tile_size, tile_size))  # Redimensiona a imagem
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.active = True  # Indica se a bomba está ativa
        self.explosao = pygame.image.load(os.path.join('Projetos/Pygame/Bomberman/assets', 'explosion.png'))
        self.explosao = pygame.transform.scale(self.explosao, (tile_size, tile_size))  # Redimensiona a imagem da explosão
        self.start_time = time.time()  # Registra o tempo de início da bomba
        self.explosao_time = None  # Registra o tempo em que a explosão ocorreu
        self.explosao_duration = 2  # Duração da explosão em segundos

    def draw(self, campo):
        if self.active:  # Desenha a bomba apenas se estiver ativa
            self.screen.blit(self.image, self.rect)
            if time.time() - self.start_time >= 3:  # Verifica se 3 segundos se passaram
                self.active = False  # A bomba explodiu
                self.explosao_time = time.time()  # Registra o tempo da explosão
                campo.destruir_blocos_ao_redor(self)  # Chama o método para destruir blocos
        elif self.explosao_time is not None:
            if time.time() - self.explosao_time < self.explosao_duration:
                # Desenha a explosão durante o tempo definido
                self.screen.blit(self.explosao, self.rect)
            else:
                self.explosao_time = None  # Reseta o tempo de explosão após sua duração

