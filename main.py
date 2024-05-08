import pygame
import sys
from constants.commonConstants import SCREEN_WIDTH, SCREEN_HEIGHT, WHITE, BLUE, RED
from utils.paddle import Paddle
from utils.ball import Ball


class BreakoutGame:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Breakout")

        self.paddle = Paddle()
        self.ball = Ball()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def update(self):
        keys = pygame.key.get_pressed()
        self.paddle.move(keys)

        self.ball.move()
        self.ball.check_collision(self.paddle)

    def render(self):
        self.screen.fill(WHITE)
        self.paddle.draw(self.screen, BLUE)
        self.ball.draw(self.screen, RED)
        pygame.display.flip()

    def run(self):
        while True:
            self.handle_events()
            self.update()
            self.render()


if __name__ == "__main__":
    game = BreakoutGame()
    game.run()
