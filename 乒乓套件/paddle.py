import pygame


class Paddle:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.speed = 5
        self.score = 0

    def draw(self, window):
        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.height))

    def update(self, up, height):
        if self.y < 0:
            self.y = 0
        elif self.y > height-self.height:
            self.y = height-self.height

        if up:
            self.y -= self.speed
            return self.y
        else:
            self.y += self.speed
            return self.y
