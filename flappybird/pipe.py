import pygame


class Pipe(pygame.sprite.Sprite):
    def __init__(self, x, y, img, top):
        super().__init__()
        self.x = x
        self.y = y
        self.top = top
        self.image = img
        self.rect = self.image.get_rect()
        if self.top:
            self.rect.bottomleft = (self.x, self.y)
        else:
            self.rect.topleft = (self.x, self.y)

        self.pipe_speed = 4

    def update(self):
        self.rect.x -= self.pipe_speed
        if self.rect.right < 0:
            self.kill()
