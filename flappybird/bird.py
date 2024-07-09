import pygame


class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y, imgs):
        super().__init__()
        self.imgs = imgs
        self.img_index = 0
        self.speed_y = 0
        self.image = self.imgs[self.img_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.last_pic_time = pygame.time.get_ticks()
        self.img_frequency = 100

    def update(self, conti):
        if conti:
            now = pygame.time.get_ticks()
            if now - self.last_pic_time > self.img_frequency:
                self.img_index += 1
                if self.img_index >= len(self.imgs):
                    self.img_index = 0
                self.image = pygame.transform.rotate(self.imgs[self.img_index], -self.speed_y * 2)
                self.last_pic_time = now

            self.speed_y += 0.5
            if self.speed_y > 9:
                self.speed_y = 9
            self.rect.y += self.speed_y
        else:
            if self.rect.y >= 460:
                self.speed_y = 0
                self.image = pygame.transform.rotate(self.imgs[self.img_index], -90)
                self.rect.y = 460
            else:
                self.speed_y = 8
                self.image = pygame.transform.rotate(self.imgs[self.img_index], -90)
                self.rect.y += self.speed_y

    def fly(self):
        self.speed_y -= 10
