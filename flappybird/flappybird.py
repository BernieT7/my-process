import pygame
import random
from bird import Bird
from pipe import Pipe


def generate_pipes(time, frequency, group):
    now = pygame.time.get_ticks()
    if now - time >= frequency:
        random_height = random.randint(-100, 100)
        pipe_btm_new = Pipe(WIDTH, HEIGHT/2 + gap/2 + random_height, pipe_btm_image, False)
        pipe_up_new = Pipe(WIDTH, HEIGHT/2 - gap/2 + random_height, pipe_up_image, True)
        group.add(pipe_btm_new)
        group.add(pipe_up_new)
        return now
    return time


def draw_score(scores):
    text = font.render(str(scores), True, WHITE)
    window.blit(text, (WIDTH/2 - text.get_width()/2, 20))


pygame.init()

WIDTH = 780
HEIGHT = 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
ground_x = 0
ground_speed = 4
ground_top = HEIGHT - 100
img_frequency = 100
gap = 150
score = 0

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("可愛的鳥鳥")

bg_img = pygame.image.load("bg.png")
bg_img = pygame.transform.scale(bg_img, (WIDTH, HEIGHT))

ground_img = pygame.image.load("ground.png")

bird_imgs = []
for i in range(1, 4):
    bird_imgs.append(pygame.image.load(f"bird{i}.png"))

pipe_btm_image = pygame.image.load("pipe.png")
pipe_up_image = pygame.transform.flip(pipe_btm_image, False, True)

restart_image = pygame.image.load("restart.png")

pygame.display.set_icon(bird_imgs[0])

FPS = 60
clock = pygame.time.Clock()

bird1 = Bird(100, HEIGHT/2, bird_imgs)
bird_group = pygame.sprite.Group()
bird_group.add(bird1)

pipe_group = pygame.sprite.Group()

pipe_frequency = 1500
last_pipe_time = pygame.time.get_ticks() - pipe_frequency

font = pygame.font.Font("微軟正黑體.ttf", 60)

conti = True
run = True
while run:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                bird1.fly()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                conti = True
                pipe_group.empty()
                bird1.rect.y = HEIGHT/2
                score = 0
                last_pipe_time = pygame.time.get_ticks() - pipe_frequency

    pipe_group.update(conti)
    reset = False
    bird_group.update(conti)
    last_pipe_time = generate_pipes(last_pipe_time, pipe_frequency, pipe_group)
    first_pipe = pipe_group.sprites()[0]

    if not first_pipe.bird_pass:
        if first_pipe.rect.right < bird1.rect.left:
            score += 1
            first_pipe.bird_pass = True

    print(first_pipe.rect.right < bird1.rect.left)

    print(score)

    ground_x -= ground_speed
    if ground_x < -100:
        ground_x = 0
    if pygame.sprite.groupcollide(bird_group, pipe_group, False, False) or\
       bird1.rect.top <= 0 or bird1.rect.bottom >= ground_top:
        conti = False
        window.blit(restart_image, (WIDTH / 2, HEIGHT / 2))
        ground_speed = 0

    window.blit(bg_img, (0, 0))
    pipe_group.draw(window)
    bird_group.draw(window)
    draw_score(score)
    window.blit(ground_img, (ground_x, ground_top))
    if not conti:
        window.blit(restart_image, (WIDTH / 2 - 150, HEIGHT / 2 - 41))
    pygame.display.update()


pygame.quit()
