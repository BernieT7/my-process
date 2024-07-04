import pygame
from ball import Ball
from paddle import Paddle


def paddle_move(key, left_paddle, right_paddle):
    global y_left
    global y_right

    if key[pygame.K_w]:
        y_left = left_paddle.update(True, HEIGHT)
    if key[pygame.K_s]:
        y_left = left_paddle.update(False, HEIGHT)

    if key[pygame.K_UP]:
        y_right = right_paddle.update(True, HEIGHT)
    if key[pygame.K_DOWN]:
        y_right = right_paddle.update(False, HEIGHT)

    ball.update(WIDTH, HEIGHT, paddle_width, paddle_height, y_left, y_right, paddle_1, paddle_2)


def draw_score(score, x, y):
    text = font.render(str(score), True, WHITE)
    window.blit(text, (x, y))


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
WIDTH = 700
HEIGHT = 500
FPS = 60
paddle_height = 100
paddle_width = 15
y_right = HEIGHT/2-paddle_height/2
y_left = HEIGHT/2-paddle_height/2

pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("乒乓球")

ball = Ball(WIDTH/2, HEIGHT/2, 10, WHITE)
paddle_1 = Paddle(10, y_left, paddle_width, paddle_height, WHITE)
paddle_2 = Paddle(WIDTH-paddle_width-10, y_right, paddle_width, paddle_height, WHITE)

font = pygame.font.Font("C:/Users/user/Desktop/my projectt/乒乓套件/微軟正黑體.ttf", 30)

clock = pygame.time.Clock()
run = True

while run:
    clock.tick(FPS)
    # 取得輸入
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    paddle_move(keys, paddle_1, paddle_2)

    # 遊戲更新
    ball.update(WIDTH, HEIGHT, paddle_width, paddle_height, y_left, y_right, paddle_1, paddle_2)
    # 畫面顯示
    window.fill(BLACK)
    ball.draw(window)
    paddle_1.draw(window)
    paddle_2.draw(window)
    draw_score(paddle_1.score, WIDTH / 4, 20)
    draw_score(paddle_2.score, 3 * WIDTH / 4, 20)
    pygame.display.update()

pygame.quit()
