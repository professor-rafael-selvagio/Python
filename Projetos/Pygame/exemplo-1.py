# Arquivo de exemplo mostrando um "loop de jogo" básico em pygame
import pygame

# Configuração do pygame
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

while running:
    # Checar por eventos
    # O evento pygame.QUIT significa que o usuário clicou no X para fechar a janela
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Preenche a tela com uma cor para apagar qualquer coisa do último frame
    screen.fill("purple")

    # RENDERIZE SEU JOGO AQUI
    '''
    Nesse bloco de código, escreva o seu código para renderizar o jogo
    '''

    # flip() a tela para colocar seu trabalho na tela
    pygame.display.flip()

    clock.tick(60)  # limita o FPS para 60

pygame.quit()
