import pygame
from config import BULLET_SPEED

class Bullet:
    def __init__(self, x, y, direction):
        self.rect = pygame.Rect(x, y, 10, 10)
        self.direction = direction

    def move(self):
        self.rect.x += BULLET_SPEED * self.direction

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), self.rect)
