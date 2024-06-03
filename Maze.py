import time
import pygame

pygame.init()
screen = pygame.display.set_mode((1080,950))
done = False
x = 30
y = 65
a = 30
b = 850
ts1 = time.time()
ts2 = time.time()
tol1 = 0
tol2 = 0


clock = pygame.time.Clock()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill((0, 0, 0))
    pressed = pygame.key.get_pressed()

    image1 = pygame.image.load("image1.png").convert()
    pl1 = image1.get_rect()
    pl1.center = (x, y)
    screen.blit(image1, pl1)
    image2 = pygame.image.load("image2.png").convert()
    pl2 = image2.get_rect()
    pl2.center = (a, b)
    screen.blit(image2, pl2)

    block1 = pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(150, 0, 60, 450))
    block2 = pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(150, 550, 60, 450))
    block3 = pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(370, 250, 60, 450))
    block4 = pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(600, 530, 60, 450))
    block5 = pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(600, 0, 60, 450))
    block6 = pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(800, 250, 60, 450))
    block7 = pygame.draw.rect(screen, (255, 255, 0), pygame.Rect(900, 448, 60, 60))
    block8 = pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(0, 0, 1100, 30))
    block9 = pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(0, 940, 1100, 20))

    Font = pygame.font.SysFont("comicsansms", 100, True)
    Title = Font.render("Maze Finder", True, (0, 0, 255))
    screen.blit(Title, (250, 0))

    Font1 = pygame.font.SysFont("comicsansms", 20, True)

    time1 = Font1.render("Time for fish:" + str(tol1), True, (0, 0, 255))
    screen.blit(time1, (230, 900))

    time2 = Font1.render("Time for kangaroo:" + str(tol2), True, (0, 0, 255))
    screen.blit(time2, (230, 870))

    s = Font.render("s", True, (0, 0, 255))
    screen.blit(s, (155, 0))

    t = Font.render("t", True, (0, 0, 255))
    screen.blit(t, (155, 90))

    a1 = Font.render("a", True, (0, 0, 255))
    screen.blit(a1, (155, 170))

    r = Font.render("r", True, (0, 0, 255))
    screen.blit(r, (155, 250))

    t1 = Font.render("t", True, (0, 0, 255))
    screen.blit(t1, (155, 330))

    e = Font.render("e", True, (0, 0, 255))
    screen.blit(e, (800, 250))

    n = Font.render("n", True, (0, 0, 255))
    screen.blit(n, (800, 330))

    d = Font.render("d", True, (0, 0, 255))
    screen.blit(d, (800, 415))

    if pl2.colliderect(block1) or pl2.colliderect(block2) or pl2.colliderect(block3) or pl2.colliderect(block4) or pl2.colliderect(block5) or pl2.colliderect(block6) or pl2.colliderect(block8) or pl2.colliderect(block7):
        if pressed[pygame.K_w]: b += 12
        if pressed[pygame.K_s]: b -= 12
        if pressed[pygame.K_a]: a += 12
        if pressed[pygame.K_d]: a -= 12

    if pl1.colliderect(block1) or pl1.colliderect(block2) or pl1.colliderect(block3) or pl1.colliderect(block4) or pl1.colliderect(block5) or pl1.colliderect(block6) or pl1.colliderect(block9) or pl1.colliderect(block7):
        if pressed[pygame.K_UP]: y += 12
        if pressed[pygame.K_DOWN]: y -= 12
        if pressed[pygame.K_LEFT]: x += 12
        if pressed[pygame.K_RIGHT]: x -= 12

    if pl1.colliderect(block7):
        x = 30
        y = 60
        te1 = time.time()
        tol1 = round(te1 - ts1, 2)
        ts1 = time.time
    if pl2.colliderect(block7):
        a = 0
        b = 860
        te2 = time.time()
        tol2 = round(te2 - ts2, 2)
        ts2 = time.time



    if pressed[pygame.K_UP]: y -= 3
    if pressed[pygame.K_DOWN]: y += 3
    if pressed[pygame.K_LEFT]: x -= 3
    if pressed[pygame.K_RIGHT]: x += 3

    if pressed[pygame.K_w]: b -= 3
    if pressed[pygame.K_s]: b += 3
    if pressed[pygame.K_a]: a -= 3
    if pressed[pygame.K_d]: a += 3








    pygame.display.flip()
    clock.tick(60)


