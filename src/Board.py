from src.Calcs import ball_collision_ods
from src.Calcs import dist
from src.Calcs import wall_collision
from src.Ball import Ball


class Board:

    def __init__(self, r, R, N, W, acc):
        self.r = r
        self.R = R
        self.N = N
        self.W = W
        self.acc = acc
        self.balls = []

    def fill(self):
        d = round(2 * self.R / (self.N + 1))
        for i in range(1, self.N + 1):
            x = d
            y = 2 * self.R - i * d
            self.balls.append(Ball(x, y, self.r, self.W))

    def draw(self, screen, color):
        for ball in self.balls:
            ball.draw(screen, color)

    def update(self):
        for i in range(len(self.balls)):
            for j in range(i+1, len(self.balls)):
                if dist(self.balls[i], self.balls[j]) < 2*self.r + self.acc:
                    self.balls[i], self.balls[j] = ball_collision_ods(self.balls[i], self.balls[j], self.r, self.acc)

        for ball in self.balls:
            ball.vx, ball.vy = wall_collision(ball, self.R)
            ball.update()