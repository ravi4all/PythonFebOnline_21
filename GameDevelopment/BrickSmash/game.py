import pygame
pygame.init()

width = 1000
height = 500
screen = pygame.display.set_mode((width, height))

red = 255,0,0
black = 0,0,0
white = 255,255,255
green = 0,255,0
color_1 = 120,140,210

def main():
    bar_width = 200
    bar_height = 20
    bar_x = width//2 - bar_width//2
    bar_y = height - bar_height - 10
    move_bar_x = 0

    ball_radius = 10
    # ball_x = bar_x + bar_width//2
    ball_y = bar_y - ball_radius
    ball_move_x = 0
    ball_move_y = 0
    move_ball = False

    brickWidth = 90
    brickHeight = 30
    rows = 5
    cols = width // brickWidth
    bricksList = []
    for i in range(rows):
        for j in range(cols):
            rect = pygame.Rect(j * (brickWidth + 5), i * (brickHeight + 5),
                        brickWidth, brickHeight)
            bricksList.append(rect)

    while True:
        if not move_ball:
            ball_x = bar_x + bar_width // 2
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    move_bar_x = -1
                elif event.key == pygame.K_RIGHT:
                    move_bar_x = 1
                elif event.key == pygame.K_SPACE:
                    move_ball = True
                    ball_move_x = 1
                    ball_move_y = -1

            else:
                move_bar_x = 0

        screen.fill(white)

        bar_rect = pygame.draw.rect(screen, red, [bar_x, bar_y, bar_width, bar_height])
        bar_x += move_bar_x

        pygame.draw.circle(screen, color_1, [ball_x, ball_y], ball_radius)
        ball_rect = pygame.Rect(ball_x, ball_y, ball_radius, ball_radius)
        ball_x += ball_move_x
        ball_y += ball_move_y

        for i in range(len(bricksList)):
            pygame.draw.rect(screen, black, bricksList[i])

        for i in range(len(bricksList)):
            if bricksList[i].colliderect(ball_rect):
                del bricksList[i]
                ball_move_y = 1
                break

        if ball_x > width - ball_radius:
            ball_move_x = -1
        elif ball_x < ball_radius:
            ball_move_x = 1
        elif ball_y > height:
            ball_move_y = -1
        elif ball_y < ball_radius:
            ball_move_y = 1
        elif ball_rect.colliderect(bar_rect):
            ball_move_y = -1

        pygame.display.update()

main()