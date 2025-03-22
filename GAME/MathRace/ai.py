import pygame
from config import AI_SPEED  # Ensure this import now works

class AI:
    def __init__(self, x, y, image_path):
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (50, 30))  # Resize car
        self.rect = self.image.get_rect(topleft=(x, y))

    def move(self):
        """Moves the AI at a constant speed"""
        self.rect.x += AI_SPEED

    def draw(self, screen):
        screen.blit(self.image, self.rect)
