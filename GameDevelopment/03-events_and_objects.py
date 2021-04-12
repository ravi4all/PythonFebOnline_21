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
while True:
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    screen.fill(white)

    # Code to Draw any object
    pygame.draw.rect(screen, red, [x,y,w,h])
    pygame.draw.circle(screen, color_1, [100,100], 50)
    pygame.display.update()
