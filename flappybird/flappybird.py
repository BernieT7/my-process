import pygame
import random
from bird import Bird
from pipe import Pipe


def generate_pipes(time, frequency, group):
    now = pygame.time.get_ticks()
    if now - time > frequency:
        random_height = random.randint(-100, 100)
        pipe_btm_new = Pipe(WIDTH, HEIGHT/2 + gap/2 + random_height, pipe_btm_image, False)
        pipe_up_new = Pipe(WIDTH, HEIGHT/2 - gap/2 + random_height, pipe_up_image, True)
        group.add(pipe_btm_new)
        group.add(pipe_up_new)
        return now
    return time


pygame.init()

WIDTH = 780
HEIGHT = 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
ground_x = 0
ground_speed = 4
img_frequency = 100
gap = 150

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("可愛的鳥鳥")

bg_img = pygame.image.load("C:/Users/user/Desktop/my projectt/flappybird/bg.png")
bg_img = pygame.transform.scale(bg_img, (WIDTH, HEIGHT))

ground_img = pygame.image.load("C:/Users/user/Desktop/my projectt/flappybird/ground.png")

bird_imgs = []
for i in range(1, 4):
    bird_imgs.append(pygame.image.load(f"C:/Users/user/Desktop/my projectt/flappybird/bird{i}.png"))

pipe_btm_image = pygame.image.load("C:/Users/user/Desktop/my projectt/flappybird/pipe.png")
pipe_up_image = pygame.transform.flip(pipe_btm_image, False, True)

pygame.display.set_icon(bird_imgs[0])

FPS = 60
clock = pygame.time.Clock()

bird1 = Bird(100, HEIGHT/2, bird_imgs)
bird_group = pygame.sprite.Group()
bird_group.add(bird1)

pipe_group = pygame.sprite.Group()

pipe_frequency = 1500
last_pipe_time = pygame.time.get_ticks() - pipe_frequency

run = True
while run:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    bird_group.update()
    pipe_group.update()
    last_pipe_time = generate_pipes(last_pipe_time, pipe_frequency, pipe_group)
    ground_x -= ground_speed
    if ground_x < -100:
        ground_x = 0

    window.blit(bg_img, (0, 0))
    bird_group.draw(window)
    pipe_group.draw(window)
    window.blit(ground_img, (ground_x, HEIGHT - 100))
    pygame.display.update()
pygame.quit()
