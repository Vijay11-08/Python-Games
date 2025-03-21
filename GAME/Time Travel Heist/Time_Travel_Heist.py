import pygame
import random
import os

# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Time Travel Heist ⏳💰")

# Colors
WHITE, BLACK, RED, GREEN, BLUE = (255, 255, 255), (0, 0, 0), (200, 0, 0), (0, 200, 0), (0, 0, 200)

# Game variables
player_speed = 4
player_health = 3  # Player health
time_periods = ["Ancient Egypt", "Medieval Europe", "Cyberpunk Future"]
current_time_period = 0
score = 0

# Load images
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
player_img = pygame.image.load(os.path.join(BASE_DIR, "player.png"))
player_img = pygame.transform.scale(player_img, (40, 60))

enemy_img = pygame.image.load(os.path.join(BASE_DIR, "guard.png"))
enemy_img = pygame.transform.scale(enemy_img, (50, 70))

# Player position
player_x, player_y = WIDTH // 2, HEIGHT - 100

# Guards
guards = [[random.randint(100, WIDTH - 100), random.randint(100, HEIGHT - 100)] for _ in range(3)]

# Treasures
treasures = [[random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50)] for _ in range(3)]

# Clock
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)

def draw_objects():
    screen.fill(BLACK)
    
    # Draw player
    screen.blit(player_img, (player_x, player_y))

    # Draw guards
    for guard in guards:
        screen.blit(enemy_img, (guard[0], guard[1]))

    # Draw treasures
    for treasure in treasures:
        pygame.draw.circle(screen, BLUE, treasure, 10)

    # Display time period
    time_text = font.render(f"Era: {time_periods[current_time_period]}", True, WHITE)
    screen.blit(time_text, (20, 20))

    # Display health
    health_text = font.render(f"Health: {player_health}", True, RED)
    screen.blit(health_text, (20, 50))

    # Display score
    score_text = font.render(f"Score: {score}", True, GREEN)
    screen.blit(score_text, (20, 80))

    pygame.display.update()

running = True
while running:
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] or keys[pygame.K_UP]: player_y -= player_speed
    if keys[pygame.K_s] or keys[pygame.K_DOWN]: player_y += player_speed
    if keys[pygame.K_a] or keys[pygame.K_LEFT]: player_x -= player_speed
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]: player_x += player_speed
    
    # Switch time periods (space key)
    if keys[pygame.K_SPACE]:
        current_time_period = (current_time_period + 1) % len(time_periods)
        pygame.time.delay(200)

    # Check for treasure collection
    for treasure in treasures[:]:  
        if pygame.Rect(player_x, player_y, 40, 60).colliderect(pygame.Rect(treasure[0], treasure[1], 10, 10)):
            treasures.remove(treasure)  
            score += 10  

    # Guard movement
    for guard in guards:
        if player_x > guard[0]: guard[0] += 1
        if player_x < guard[0]: guard[0] -= 1
        if player_y > guard[1]: guard[1] += 1
        if player_y < guard[1]: guard[1] -= 1

    # Check for guard collision (Lose health)
    for guard in guards:
        if pygame.Rect(player_x, player_y, 40, 60).colliderect(pygame.Rect(guard[0], guard[1], 50, 70)):
            player_health -= 1
            player_x, player_y = WIDTH // 2, HEIGHT - 100  # Reset position
            pygame.time.delay(500)

    # Check for win or loss
    if player_health <= 0:
        screen.fill(BLACK)
        game_over_text = font.render("Game Over! 💀", True, RED)
        screen.blit(game_over_text, (WIDTH//2 - 60, HEIGHT//2))
        pygame.display.update()
        pygame.time.delay(2000)
        running = False

    if len(treasures) == 0:
        screen.fill(BLACK)
        win_text = font.render("You Stole All Artifacts! 🎉", True, GREEN)
        screen.blit(win_text, (WIDTH//2 - 120, HEIGHT//2))
        pygame.display.update()
        pygame.time.delay(2000)
        running = False

    draw_objects()
    clock.tick(30)

pygame.quit()
