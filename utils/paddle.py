import pygame
from constants.commonConstants import (
    SCREEN_WIDTH,
    PADDLE_WIDTH,
    PADDLE_HEIGHT,
    PADDLE_SPEED,
    SCREEN_HEIGHT,
)


class Paddle:
    def __init__(self):
        self.rect = pygame.Rect(
            SCREEN_WIDTH // 2 - PADDLE_WIDTH // 2,
            SCREEN_HEIGHT - 50,
            PADDLE_WIDTH,
            PADDLE_HEIGHT,
        )

    def move(self, keys):
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= PADDLE_SPEED
        if keys[pygame.K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.x += PADDLE_SPEED

    def draw(self, screen, color):
        pygame.draw.rect(screen, color, self.rect)
