import pygame
import random

pygame.init()

width = 1000
height = 500
screen = pygame.display.set_mode((width, height))

# rgb - red,green,blue  (0 - 255)
red = 255, 0, 0
black = 0, 0, 0
white = 255, 255, 255
green = 0, 255, 0
color_1 = 120, 140, 210

x = 0
y = 0
w = 50
h = 50
move_x = 1
move_y = 0

frog_img = pygame.image.load('frog.png')
frog_w = frog_img.get_width()
frog_h = frog_img.get_height()
frog_x = random.randint(0, width - frog_w)
frog_y = random.randint(0, height - frog_h)

snakeList = []
snakeLength = 1

def draw_snake(snakeList):
    for i in range(len(snakeList)):
        pygame.draw.rect(screen, red, [snakeList[i][0], snakeList[i][1],
                                       w, h])

clock = pygame.time.Clock()
FPS = 200
while True:
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                move_x = 1
                move_y = 0
            elif event.key == pygame.K_LEFT:
                move_x = -1
                move_y = 0
            elif event.key == pygame.K_DOWN:
                move_y = 1
                move_x = 0
            elif event.key == pygame.K_UP:
                move_y = -1
                move_x = 0

    screen.fill(white)

    # Code to Draw any object
    snake_rect = pygame.draw.rect(screen, red, [x, y, w, h])

    screen.blit(frog_img, (frog_x, frog_y))
    frog_rect = pygame.Rect(frog_x, frog_y, frog_w, frog_h)

    if frog_rect.colliderect(snake_rect):
        frog_x = random.randint(0, width - frog_w)
        frog_y = random.randint(0, height - frog_h)
        snakeLength += 10
        FPS += 50

    x += move_x
    y += move_y

    snakeHead = []
    snakeHead.append(x)
    snakeHead.append(y)

    snakeList.append(snakeHead)

    if len(snakeList) > snakeLength:
        del snakeList[0]

    draw_snake(snakeList)

    if x > width:
        x = -50
    elif x < -50:
        x = width

    if y > height:
        y = -50
    elif y < -50:
        y = height

    pygame.display.update()
    clock.tick(FPS)
