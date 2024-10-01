# Arquivo de exemplo mostrando um círculo se movendo na tela
import pygame

# Configuração do pygame
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:
    # Checar por eventos
    # O evento pygame.QUIT significa que o usuário clicou no X para fechar a janela
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Preenche a tela com uma cor para apagar qualquer coisa do último frame
    screen.fill("purple")

    pygame.draw.circle(screen, "red", player_pos, 40)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt

    # flip() a tela para colocar seu trabalho na tela
    pygame.display.flip()

    # limita o FPS para 60
    # dt é o tempo delta em segundos desde o último frame, usado para 
    # física independente da taxa de quadros.
    dt = clock.tick(60) / 1000

pygame.quit()