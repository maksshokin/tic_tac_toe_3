import pygame
import random

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("TICTACTOE")
icon =pygame.image.load('Images/icon.png')
pygame.display.set_icon(icon)

line_gorizontal = pygame.Surface((600, 1))
line_gorizontal.fill((0, 0, 0))
line_vertical = pygame.Surface((1, 600))
line_vertical.fill((0, 0, 0))

running = True
while running:
    screen.fill((210,180,230))

    screen.blit(line_gorizontal, (0, 200))
    screen.blit(line_gorizontal, (0, 400))
    screen.blit(line_vertical, (200, 0))
    screen.blit(line_vertical, (400, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.QUIT
            running = False
    pygame.display.update()

