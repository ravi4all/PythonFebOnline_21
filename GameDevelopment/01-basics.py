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

while True:
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    screen.fill(red)
    pygame.display.update()
