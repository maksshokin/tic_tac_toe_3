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

#bg_sound = pygame.mixer.Sound('sounds/bg.mp3')
#bg_sound.play()

def Tic(coordinates):
    """Отрисовка круга с центром на заданных координатах."""
    pygame.draw.circle(surface=screen, color=(0, 0, 0), width=1, radius=75, center=(coordinates))

def Tac(coordinates):
    """Отрисовка крестика с центром на заданных координатах."""
    st_coord_1 = coordinates[0] - 50
    st_coord_2 = coordinates[1] - 50
    ed_coord_1 = coordinates[0] + 50
    ed_coord_2 = coordinates[1] + 50
    start_pose_1 = (st_coord_1, st_coord_2)
    end_pose_1   = (ed_coord_1, ed_coord_2)
    start_pose_2 = (st_coord_1, ed_coord_2)
    end_pose_2   = (ed_coord_1, st_coord_2)
    pygame.draw.line(surface=screen,color=(0, 0, 0), start_pos=start_pose_1, end_pos=end_pose_1)
    pygame.draw.line(surface=screen,color=(0, 0, 0), start_pos=start_pose_2, end_pos=end_pose_2)

def coord_maker(j, i):
    """Функция, возвращающая координаты центров фигур на дисплее"""
    print(j, i)
    if   j== 0 and i == 0:
        return (100, 100)
    elif j== 0 and i == 1:
        return (300, 100)
    elif j== 0 and i == 2:
        return (500, 100)
    elif j== 1 and i == 0:
        return (100, 300)
    elif j== 1 and i == 1:
        return (300, 300)
    elif j== 1 and i == 2:
        return (500, 300)
    elif j== 2 and i == 0:
        return (100, 500)
    elif j== 2 and i == 1:
        return (300, 500)
    elif j== 2 and i == 2:
        return (500, 500)

engaged = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
engaged_type = engaged
count = 0
running = True
while running:
    screen.fill((210,180,230))
    clock.tick(60)
    screen.blit(line_gorizontal, (0, 200))
    screen.blit(line_gorizontal, (0, 400))
    screen.blit(line_vertical, (200, 0))
    screen.blit(line_vertical, (400, 0))
    
    count_i = -1
    for i in engaged:
        count_i += 1
        count_j = -1
        for j in i:
            count_j += 1
            if j == 1:
                if engaged_type[count_i][count_j] == 1:
                    Tac(coord_maker(count_j, count_i))
                else:
                    Tic(coord_maker(count_j, count_i))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.QUIT
            running = False
        elif event.type == pygame.MOUSEMOTION:
            cursor_pos = event.pos
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if cursor_pos[0] < 200:
                    if cursor_pos[1] < 200:
                        if not engaged[0][0] == 1:
                            engaged[0][0] = 1
                            count += 1
                            if count % 2 == 0:
                                engaged_type[0][0] = 0
                            else:
                                engaged_type[0][0] = 1
                    elif cursor_pos[1] < 400:
                        if not engaged[0][1] == 1:
                            engaged[0][1] = 1
                            count += 1
                            if count % 2 == 0:
                                engaged_type[0][1] = 0
                            else:
                                engaged_type[0][1] = 1
                    else:
                        if not engaged[0][2] == 1:
                            engaged[0][2] = 1
                            count += 1
                            if count % 2 == 0:
                                engaged_type[0][2] = 0
                            else:
                                engaged_type[0][2] = 1
                elif cursor_pos[0] < 400:
                    if cursor_pos[1] < 200:
                       if not engaged[1][0] == 1:
                            count += 1
                            engaged[1][0] = 1
                            if count % 2 == 0:
                                engaged_type[1][0] = 0
                            else:
                                engaged_type[1][0] = 1
                    elif cursor_pos[1] < 400:
                       if not engaged[1][1] == 1:
                            engaged[1][1] = 1
                            count += 1
                            if count % 2 == 0:
                                engaged_type[1][1] = 0
                            else:
                                engaged_type[1][1] = 1
                    else:
                       if not engaged[1][2] == 1:
                            engaged[1][2] = 1
                            count += 1
                            if count % 2 == 0:
                                engaged_type[1][2] = 0
                            else:
                                engaged_type[1][2] = 1
                else:
                    if cursor_pos[1] < 200:
                        if not engaged[2][0] == 1:
                            engaged[2][0] = 1
                            count += 1
                            if count % 2 == 0:
                                engaged_type[2][0] = 0
                            else:
                                engaged_type[2][0] = 1
                    elif cursor_pos[1] < 400:
                        if not engaged[2][1] == 1:
                            engaged[2][1] = 1
                            count += 1
                            if count % 2 == 0:
                                engaged_type[2][1] = 0
                            else:
                                engaged_type[2][1] = 1
                    else:
                        if not engaged[2][2] == 1:
                            engaged[2][2] = 1
                            count += 1
                            if count % 2 == 0:
                                engaged_type[2][2] = 0
                            else:
                                engaged_type[2][2] = 1
    pygame.display.update()

