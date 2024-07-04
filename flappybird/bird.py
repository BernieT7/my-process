import pygame


class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y, imgs):
        super().__init__()
        self.imgs = imgs
        self.img_index = 0
        self.image = self.imgs[self.img_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.last_pic_time = pygame.time.get_ticks()
        self.img_frequency = 100

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_pic_time > self.img_frequency:
            self.img_index += 1
            if self.img_index >= len(self.imgs):
                self.img_index = 0
            self.image = self.imgs[self.img_index]
            self.last_pic_time = now
