import pygame
import random


class Ball:
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        random_list = [-4, -3, -2, -1, 1, 2, 3, 4]
        self.speed_x = random.choice(random_list)
        self.speed_y = random.choice(random_list)

    def draw(self, window):
        pygame.draw.circle(window, self.color, (self.x, self.y), self.radius)

    def update(self, width, height, paddle_width, paddle_height, y_left, y_right, left_paddle, right_paddle):
        self.x += self.speed_x
        self.y += self.speed_y
        ball_top = self.y - self.radius
        ball_bot = self.y + self.radius
        ball_left = self.x - self.radius
        ball_right = self.x + self.radius

        if ball_bot > height or ball_top < 0:
            self.speed_y *= -1

        if ball_right > width - 10 - paddle_width and ball_right < width - 10 and self.y-10 < y_right + paddle_height and self.y-10 > y_right:
            self.speed_x *= -1
            self.speed_y = random.randint(-5, 5)

        if ball_left < 10 + paddle_width and ball_left > 10 and self.y-10 < y_left + paddle_height and self.y-10 > y_left:
            self.speed_x *= -1
            self.speed_y = random.randint(-5, 5)

        if ball_right < 0:
            right_paddle.score += 1
            self.reset(width, height)

        if ball_left > width:
            left_paddle.score += 1
            self.reset(width, height)

    def reset(self, width, height):
        self.x = width / 2
        self.y = height / 2
        random_list = [-4, -3, -2, -1, 1, 2, 3, 4]
        self.speed_x = random.choice(random_list)
        self.speed_y = random.choice(random_list)
