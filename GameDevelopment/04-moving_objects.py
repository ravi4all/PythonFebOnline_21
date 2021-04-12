import pygame
pygame.init()

width = 1000
height = 500
screen = pygame.display.set_mode((width, height))

# rgb - red,green,blue  (0 - 255)
red = 255,0,0
black = 0,0,0
white = 255,255,255
green = 0,255,0
color_1 = 120,140,210

x = 0
y = 0
w = 50
h = 50
move_x = 1
move_y = 1

clock = pygame.time.Clock()
FPS = 100
while True:
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    screen.fill(white)

    # Code to Draw any object
    pygame.draw.rect(screen, red, [x,y,w,h])

    x += move_x
    y += move_y

    if x > width - 50:
        move_x = -1
    elif x < 0:
        move_x = 1

    if y > height - 50:
        move_y = -1
    elif y < 0:
        move_y = 1

    pygame.display.update()
    clock.tick(FPS)
