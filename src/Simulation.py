import pygame
import sys


class Simulation:

    def __init__(self, board):
        self.board = board
        self.pause = False
        self.clockt = 60

    def start(self):
        self.board.fill()
        pygame.init()
        screen = pygame.display.set_mode((2 * self.board.R, 2 * self.board.R))
        screen.fill((0, 0, 0))
        color = (0, 255, 0)
        font = pygame.font.SysFont("monospace", 25)
        clock = pygame.time.Clock()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        sys.exit()
                    else:
                        self.pause = not self.pause
            if not self.pause:
                self.board.update()
                screen.fill((0, 0, 0))
                text = font.render("energia kin: " + str(round(sum(ball.v ** 2 for ball in self.board.balls))), 1, (255, 0, 0))
                screen.blit(text, (600, 950))
                self.board.draw(screen, color)
                pygame.display.update()
                clock.tick(self.clockt)
                # pause = not pause