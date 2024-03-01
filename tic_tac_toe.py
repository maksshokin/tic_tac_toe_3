import pygame

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("TICTACTOE")
icon =pygame.image.load('Images/icon.png')
pygame.display.set_icon(icon)

clock = pygame.time.Clock()

def filling_black(object):
    object.fill((0, 0, 0))

line_gorizontal = pygame.Surface((600, 1))
line_vertical = pygame.Surface((1, 600))
filling_black(line_gorizontal)
filling_black(line_vertical)

coordinate = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

#bg_sound = pygame.mixer.Sound('sounds/bg.mp3')
#bg_sound.play()

def Tic(coordinates):
    pygame.draw.circle(surface=screen, color=(0, 0, 0), width=1, radius=100, center=(coordinates))

def Tac(coordinates):
    pass

Tic((150, 150))

running = True
while running:
    screen.fill((210,180,230))
    clock.tick(60)
    screen.blit(line_gorizontal, (0, 200))
    screen.blit(line_gorizontal, (0, 400))
    screen.blit(line_vertical, (200, 0))
    screen.blit(line_vertical, (400, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.QUIT
            running = False
        elif event.type == pygame.MOUSEMOTION:
            cursor_pos = event.pos
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                print(cursor_pos)
                Tic((100, 100))
                
    pygame.display.update()

