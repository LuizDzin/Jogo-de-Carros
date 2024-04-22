import pygame
import random
import game

def start_game():
    # Inicia o jogo aqui
    print("Jogo iniciado!")
    
pygame.init()

w,h = 1100, 900
BACKGROUND_COLOR = (0, 0, 0)

icon = pygame.image.load("icon.png")

pygame.display.set_icon(icon)

screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("Jogo de Carros")

# Carrega a imagem de fundo
background = pygame.image.load('intro.png')

# Redimensiona a imagem de fundo para se ajustar à tela
background = pygame.transform.scale(background, (w, h))

running = True
while running:
    screen.fill(BACKGROUND_COLOR)

    # Desenha a imagem de fundo na tela
    screen.blit(background, (0, 0))
    
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()