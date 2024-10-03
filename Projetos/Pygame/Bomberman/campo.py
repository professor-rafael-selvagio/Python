import pygame
import random
import os

# Definindo a classe BlocoDestrutivel
class BlocoDestrutivel:
    def __init__(self, screen, tile_size, x, y):
        self.screen = screen
        self.tile_size = tile_size
        self.rect = pygame.Rect(x, y, tile_size, tile_size)  # Cria um retângulo para a posição do bloco

    def draw(self):
        # Desenha um retângulo verde para representar o bloco destrutível
        pygame.draw.rect(self.screen, (0, 255, 0), self.rect)

# Definindo a classe Campo responsável por desenhar o campo de batalha
class Campo:
    def __init__(self, screen, tile_size, largura, altura):
        self.screen = screen
        self.tile_size = tile_size
        self.largura = largura
        self.altura = altura
        self.blocos = []  # Armazenar as posições dos blocos indestrutíveis
        self.blocos_destrutiveis = []  # Armazenar os objetos de blocos destrutíveis

    def get_blocos_destrutiveis(self):
        return self.blocos_destrutiveis

    def get_blocos_indestrutiveis(self):
        return self.blocos

    def desenhar_campo(self):
        # Limpa a tela
        self.screen.fill((255, 255, 255))  # Preenche o fundo de branco
        
        # Desenhar o campo vazio
        for y in range(0, self.altura):
            for x in range(0, self.largura):
                # Desenhar um espaço vazio
                rect = pygame.Rect(x * self.tile_size, y * self.tile_size, self.tile_size, self.tile_size)

                # Adicionar blocos indestrutíveis nas posições especificadas
                if y in [1, 3, 5, 7, 9, 11] and x in [1, 3, 5, 7, 9, 11]:
                    pygame.draw.rect(self.screen, (128, 128, 128), rect)  # Bloco não quebrável (cinza)

                # Desenhar blocos destrutíveis
                for bloco in self.blocos_destrutiveis:
                    bloco.draw()  # Desenha os blocos destrutíveis

    # Exemplo de como adicionar blocos destrutíveis na classe Campo
    def adicionar_blocos_destrutiveis(self):
        # Total de blocos disponíveis
        total_blocos = (self.largura * (self.altura - 1))  # Total de blocos (sem contar a última linha)
        total_indestrutiveis = len(self.blocos)  # Total de blocos indestrutíveis
        num_blocos_destrutiveis = int((total_blocos - total_indestrutiveis) * 0.9)  # 90% de blocos destrutíveis

        # Posições que não podem ter blocos destrutíveis
        posicoes_ocupadas = set(self.blocos) | {(0, 0), (0, 1), (1, 0), (0, 10), (0, 11), (1, 11)}

        # Adicionando blocos destrutíveis nas posições disponíveis
        while len(self.blocos_destrutiveis) < num_blocos_destrutiveis:
            x = random.randint(0, self.largura - 1)
            y = random.randint(0, self.altura - 1)  # -2 porque a última linha é vazia

            # Verifica se a posição está disponível
            if (x, y) not in posicoes_ocupadas and (x, y) not in self.blocos_destrutiveis:
                bloco = BlocoDestrutivel(self.screen, self.tile_size, x * self.tile_size, y * self.tile_size)
                self.blocos_destrutiveis.append(bloco)  # Armazena a instância do bloco destrutível

        # Desenhar blocos destrutíveis
        for bloco in self.blocos_destrutiveis:
            bloco.draw()  # Desenha os blocos destrutíveis


        print(f"Número de blocos destrutíveis adicionados: {len(self.blocos_destrutiveis)}")

    def destruir_blocos_ao_redor(self, bomba):
        bomba_rect = bomba.rect
        # Verifica as posições em relação à bomba
        for bloco in self.blocos_destrutiveis[:]:  # Itera sobre uma cópia da lista
            if bloco.rect.colliderect(bomba_rect):
                self.blocos_destrutiveis.remove(bloco)  # Remove o bloco se colidir com a bomba
                self.desenhar_campo()  # Desenha o campo novamente após a destruição do bloco
                bloco.draw()  # Redesenha o bloco, se necessário

