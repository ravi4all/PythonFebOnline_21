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

bg_img = pygame.image.load('img.jpg')
bg_img = pygame.transform.scale(bg_img, (width, height))

font = pygame.font.Font('font_1.ttf',52)
title = font.render('Batman : The Dark Knight', True, white)

pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play()

while True:
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # screen.fill(red)
    screen.blit(bg_img, (0,0))
    screen.blit(title, (250,50))
    pygame.display.update()
