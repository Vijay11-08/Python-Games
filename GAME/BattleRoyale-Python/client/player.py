import pygame
from config import PLAYER_SPEED

class Player:
    def __init__(self, x, y, color):
        self.rect = pygame.Rect(x, y, 20, 20)
        self.color = color

    def move(self, keys):
        if keys[pygame.K_LEFT]: self.rect.x -= PLAYER_SPEED
        if keys[pygame.K_RIGHT]: self.rect.x += PLAYER_SPEED
        if keys[pygame.K_UP]: self.rect.y -= PLAYER_SPEED
        if keys[pygame.K_DOWN]: self.rect.y += PLAYER_SPEED

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
