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

font = pygame.font.SysFont("comicsans", 30, True, False)


def food(fx, fy):
    
    pygame.draw.rect(win, (BLACK), (fx, fy, snakeDimension, snakeDimension))

def drawSnake(x, y):

    pygame.draw.rect(win, (BLACK), (x, y, snakeDimension, snakeDimension))

def text_object(msg, color):
    
    txtSurf = font.render(msg, True, color)
    return txtSurf, txtSurf.get_rect()

def display_text(msg, color, y_displace = 0, x_displace = 0):
    
    textSurf, textRect = text_object(msg, color)
    textRect.center = W/2 + x_displace, H/2 + y_displace

    win.blit(textSurf, textRect)

def die(score):

    die = True
    
    while die:

        clock.tick(5)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    die = False
                    main()

        win.fill(WHITE)
        display_text("Your Score is " + str(score), BLACK, y_displace = 20)
        display_text("Press SPACE BAR to continue", BLACK, y_displace = -20)

        pygame.display.update()

def drawScreen(x, y, fx, fy, snakeLength, snake, score):

    win.fill(WHITE)

    display_text("Score: " + str(score), (0, 255, 0), y_displace=-1 * round(H / 2.2), x_displace=round(W/2.5))

    food(fx, fy)

    for snk in snake:
        drawSnake(snk[0], snk[1])

    pygame.display.update()

def main():

    x = 100
    y = 100

    snake = []
    snakeLength = 1

    sVel = 10

    sHor = 1
    sVer = 0

    rx = random.randint(0, W - snakeDimension)
    fx = round(rx / snakeDimension) * snakeDimension

    ry = random.randint(0, H - snakeDimension)
    fy = round(ry / snakeDimension) * snakeDimension

    score = 0

    run = True

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

                elif event.key == pygame.K_RIGHT:
                    sHor = 1
                    sVer = 0

                elif event.key == pygame.K_UP:
                    sVer = -1
                    sHor = 0

                elif event.key == pygame.K_DOWN:
                    sVer = 1
                    sHor = 0

        x += sHor * sVel
        y += sVer * sVel

        if (x > W - snakeDimension or x < 0 or y > H - snakeDimension or y < 0):
            run = False
            die(score)

        snakeHead = []
        snakeHead.append(x)
        snakeHead.append(y)

        for snk in snake:
             if (snakeHead[0] == snk[0] and snakeHead[1] == snk[1]):
                 die(score)

        snake.append(snakeHead)
        

        if len(snake) > snakeLength:
            del snake[0]

        if (fx == x and fy == y):
            rx = random.randint(0, W - snakeDimension)
            fx = round(rx / snakeDimension) * snakeDimension

            ry = random.randint(0, H - snakeDimension)
            fy = round(ry / snakeDimension) * snakeDimension

            snakeLength += 1
            score += 1

        drawScreen(x, y, fx, fy, snakeLength, snake, score)

main()
