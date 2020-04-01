import math
import pygame
from src.Calcs import gen_velocity


class Ball:
    def __init__(self, x, y, r, W):
        self.x = x
        self.y = y
        self.r = r
        self.vx, self.vy = gen_velocity(W)
        self.v = math.sqrt(self.vx**2 + self.vy**2)

    def draw(self, screen, color):
        pygame.draw.circle(screen, color, (self.x, self.y), self.r, 0)

    def update(self):
        self.x = round(self.x + self.vx)
        self.y = round(self.y + self.vy)
        self.v = math.sqrt(self.vx ** 2 + self.vy ** 2)