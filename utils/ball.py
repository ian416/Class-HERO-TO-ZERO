import pygame
from constants.commonConstants import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    BALL_SPEED_X,
    BALL_SPEED_Y,
    BALL_RADIUS,
)

class Ball:
    def __init__(self):
        self.rect = pygame.Rect(
            SCREEN_WIDTH // 2 - BALL_RADIUS,
            SCREEN_HEIGHT // 2 - BALL_RADIUS,
            BALL_RADIUS * 2,
            BALL_RADIUS * 2,
        )
        self.speed_x = BALL_SPEED_X
        self.speed_y = BALL_SPEED_Y

    def move(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

    def check_collision(self, paddle):
        if self.rect.left <= 0 or self.rect.right >= SCREEN_WIDTH:
            self.speed_x = -self.speed_x
        if self.rect.top <= 0:
            self.speed_y = -self.speed_y
        if self.rect.colliderect(paddle.rect) and self.speed_y > 0:
            self.speed_y = -self.speed_y

    def draw(self, screen, color):
        pygame.draw.ellipse(screen, color, self.rect)
