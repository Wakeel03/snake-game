import pygame
import time
import random

pygame.init()

winW = 500
winH = 500

snakeW = 10
snakeH = 10

win = pygame.display.set_mode((winW, winH))
pygame.display.set_caption("Snake")

font = pygame.font.SysFont(None, 25)

def drawSnake(snake_x, snake_y):
     pygame.draw.rect(win, (0, 0, 0), (snake_x, snake_y, snakeW, snakeH))

def drawScreen(snake_x, snake_y, food, score, snakeList):
     win.fill((255, 255, 255))
     score_text = font.render("Score: " + str(score), True, (0, 255, 0))
     win.blit(score_text, [400, 30])
     pygame.draw.rect(win, (255, 0, 0), (food[0], food[1], 10, 10))
     for snake in snakeList:
          drawSnake(snake[0], snake[1])
     pygame.display.update()

def gameOver():
     GO = True

     while GO:
          win.fill((0, 0, 0))
          screen_text = font.render("GameOver Press SpaceBar to continue", True, (255, 0, 0))
          win.blit(screen_text, [winW/3, winH/2])
          pygame.display.update()

          for event in pygame.event.get():
               if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                         GO = False
                         main()

def main():
     snakeDirX = 1
     snakeDirY = 1
     snake_vel = 10
     moveX = True
     moveY = False

     snakeLength = 1
     snakeList =[]

     foodX = round(random.randrange(0, winW - 10)/10.0) * 10.0
     foodY = round(random.randrange(0, winH - 10)/10.0) * 10.0
     
     run = True
     
     clock = pygame.time.Clock()

     snake_x = 10
     snake_y = 10

     score = 0
     
     while run:
          clock.tick(15)

          for event in pygame.event.get():
               if event.type == pygame.QUIT:
                    run = False
               if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                         snakeDirX = -1
                         moveX = True
                         moveY = False
                         
                    elif event.key == pygame.K_RIGHT:
                         snakeDirX = 1
                         moveX = True
                         moveY = False
                         
                    elif event.key == pygame.K_UP:
                         snakeDirY = -1
                         moveX = False
                         moveY = True
                         
                    elif event.key == pygame.K_DOWN:
                         snakeDirY = 1
                         moveX = False
                         moveY = True

          if moveX:
               snake_x += snake_vel * snakeDirX
          else:
               snake_y += snake_vel * snakeDirY

          food = [foodX, foodY]

          snakeHead = [snake_x, snake_y]
          snakeList.append(snakeHead)

          if len(snakeList) > snakeLength:
               del snakeList[0]

          for snake in snakeList[:-1]:
               if snakeHead[0] == snake[0] and snakeHead[1] == snake[1]:
                    run = False
                    gameOver()
          

          if snake_x == food[0] and snake_y == food[1]:
               foodX = round(random.randrange(0, winW - 10)/10.0) * 10.0
               foodY = round(random.randrange(0, winH - 10)/10.0) * 10.0
               snakeLength += 1
               score += 1
          

          if snake_x > winW or snake_x < 0 or snake_y > winH or snake_y < 0:
               run = False
               gameOver()

          drawScreen(snake_x, snake_y, food, score, snakeList)

main()

