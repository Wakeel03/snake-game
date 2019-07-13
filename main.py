import pygame
import random

pygame.init()

W = 800
H = 800
fps = 30

win = pygame.display.set_mode((W, H))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

snakeDimension = 10
snake = []

x = 100
y = 100

sVel = 10

sHor = 1
sVer = 0

rx = random.randint(0, W - snakeDimension)
fx = round(rx / snakeDimension) * snakeDimension

ry = random.randint(0, H - snakeDimension)
fy = round(ry / snakeDimension) * snakeDimension

run = True

def food(fx, fy):
    
    pygame.draw.rect(win, (BLACK), (fx, fy, snakeDimension, snakeDimension))

def drawSnake(x, y):

    pygame.draw.rect(win, (BLACK), (x, y, snakeDimension, snakeDimension))

def drawScreen(x, y, fx, fy):

    win.fill(WHITE)

    food(fx, fy)

    drawSnake(x, y)

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
                sHor = -1
                sVer = 0

            if event.key == pygame.K_RIGHT:
                sHor = 1
                sVer = 0

            if event.key == pygame.K_UP:
                sVer = -1
                sHor = 0

            if event.key == pygame.K_DOWN:
                sVer = 1
                sHor = 0

    x += sHor * sVel
    y += sVer * sVel

    if (fx == x and fy == y):
        rx = random.randint(0, W - snakeDimension)
        fx = round(rx / snakeDimension) * snakeDimension

        ry = random.randint(0, H - snakeDimension)
        fy = round(ry / snakeDimension) * snakeDimension

    drawScreen(x, y, fx, fy)
