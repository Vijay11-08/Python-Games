import pygame
import random

# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dimension Drifter 🌌🔮")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (200, 0, 0)
BLUE = (0, 0, 200)
GREEN = (0, 200, 0)

# Game variables
player_speed = 5
gravity_levels = [0.5, 1.5, -0.5]  # Different gravity in dimensions
dimension = 0  # Current dimension (index)
portal_active = False

# Load player image
player = pygame.Rect(WIDTH // 2, HEIGHT - 60, 40, 60)
velocity_y = 0
on_ground = False

# Collectible energy shards
shards = [pygame.Rect(random.randint(100, WIDTH - 100), random.randint(100, HEIGHT - 100), 15, 15) for _ in range(3)]

# Portal
portal = pygame.Rect(WIDTH - 100, HEIGHT // 2, 50, 50)

# Clock
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)

def draw_objects():
    screen.fill(BLACK)
    
    # Draw player
    pygame.draw.rect(screen, BLUE, player)
    
    # Draw shards
    for shard in shards:
        pygame.draw.rect(screen, GREEN, shard)
    
    # Draw portal
    if portal_active:
        pygame.draw.rect(screen, RED, portal)
    
    # Display current dimension
    dimension_text = font.render(f"Dimension: {dimension + 1}", True, WHITE)
    screen.blit(dimension_text, (20, 20))
    
    pygame.display.update()

# Game loop
running = True
while running:
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        player.x -= player_speed
    if keys[pygame.K_d]:
        player.x += player_speed
    if keys[pygame.K_SPACE] and on_ground:
        velocity_y = -10
        on_ground = False
    
    # Gravity effect
    velocity_y += gravity_levels[dimension]
    player.y += velocity_y
    if player.y >= HEIGHT - player.height:
        player.y = HEIGHT - player.height
        velocity_y = 0
        on_ground = True
    
    # Dimension switching
    if keys[pygame.K_TAB]:
        dimension = (dimension + 1) % len(gravity_levels)
        pygame.time.delay(200)
    
    # Check for shard collection
    for shard in shards[:]:
        if player.colliderect(shard):
            shards.remove(shard)
    
    # Activate portal when all shards are collected
    if not shards:
        portal_active = True
    
    # Check portal entry
    if portal_active and player.colliderect(portal):
        print("You escaped! 🎉")
        running = False
    
    draw_objects()
    clock.tick(30)

pygame.quit()   