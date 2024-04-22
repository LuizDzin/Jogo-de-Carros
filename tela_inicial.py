import pygame
import random
import game

pygame.init()

WIDTH, HEIGHT = 1100, 900
BACKGROUND_COLOR = (0, 0, 0)

icon = pygame.image.load("icon.png")

pygame.display.set_icon(icon)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jogo de Carros")

# Carrega a imagem de fundo
background = pygame.image.load('intro.png')

# Redimensiona a imagem de fundo para se ajustar à tela
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

# Define as propriedades do botão
button_color = (0, 255, 0)
button_width, button_height = 100, 50
button_x, button_y = (WIDTH // 2) - (button_width // 2), (HEIGHT // 2) - (button_height // 2)

running = True
while running:
    screen.fill(BACKGROUND_COLOR)

    # Desenha a imagem de fundo na tela
    screen.blit(background, (0, 0))

    # Desenha o botão na tela
    pygame.draw.rect(screen, button_color, pygame.Rect(button_x, button_y, button_width, button_height))

    # Verifica se o mouse está sobre o botão
    mouse_pos = pygame.mouse.get_pos()
    if button_x < mouse_pos[0] < button_x + button_width and button_y < mouse_pos[1] < button_y + button_height:
        # Muda a cor do botão para indicar que o mouse está sobre ele
        pygame.draw.rect(screen, (0, 255, 255), pygame.Rect(button_x, button_y, button_width, button_height))

        # Verifica se o botão foi clicado
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Inicia o jogo
                game.start_game()

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()