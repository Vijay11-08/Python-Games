import pygame
from config import PLAYER_SPEED  # Ensure this import now works

class Player:
    def __init__(self, x, y, image_path):
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (50, 30))  # Resize car
        self.rect = self.image.get_rect(topleft=(x, y))
    
    def move(self, boost=0):
        """Moves the car based on speed boost"""
        self.rect.x += PLAYER_SPEED + boost  # Moves the player faster if they answer correctly

    def draw(self, screen):
        screen.blit(self.image, self.rect)
