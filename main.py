import pygame

pygame.init()

W = 800
H = 800
fps = 30

win = pygame.display.set_mode((W, H))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

run = True

def drawScreen():

    win.fill(WHITE)

    pygame.display.update()

while run:

    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                pass

            if event.key == pygame.K_RIGHT:
                pass

            if event.key == pygame.K_UP:
                pass

            if event.key == pygame.K_DOWN:
                pass

    drawScreen()
