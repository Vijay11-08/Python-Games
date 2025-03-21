import pygame
import random
import math
import os

# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dream Hacker 🧠💭")

# Colors
WHITE, BLACK, RED, GREEN, BLUE = (255, 255, 255), (0, 0, 0), (200, 0, 0), (0, 200, 0), (0, 0, 200)

# Game properties
player_size = (40, 60)
player_speed = 4
player_health = 100
wave = 1
memory_pieces = 3

disturbance_meter = 0

disturbance_limit = 100
health_loss_per_hit = 10

# Get the directory of the script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Load images
player_img = pygame.image.load(os.path.join(BASE_DIR, "player.png"))
player_img = pygame.transform.scale(player_img, player_size)

enemy_img = pygame.image.load(os.path.join(BASE_DIR, "monster.png"))
enemy_img = pygame.transform.scale(enemy_img, (50, 70))

# Player Position
player_x, player_y = WIDTH // 2, HEIGHT - 100

# AI Enemies (Subconscious Monsters)
def spawn_enemies(num):
    return [[random.randint(100, WIDTH - 100), random.randint(100, HEIGHT - 100)] for _ in range(num)]

enemies = spawn_enemies(3)

# Memory Fragments (Hidden in the Dream World)
memory_fragments = [[random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50)] for _ in range(memory_pieces)]

# Clock
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)

def draw_objects():
    screen.fill(BLACK)
    
    # Draw player
    screen.blit(player_img, (player_x, player_y))

    # Draw enemies
    for enemy in enemies:
        screen.blit(enemy_img, (enemy[0], enemy[1]))

    # Draw Memory Pieces
    for memory in memory_fragments:
        pygame.draw.circle(screen, BLUE, memory, 10)

    # Draw Health Bar
    pygame.draw.rect(screen, GREEN, (20, 20, player_health * 2, 20))
    pygame.draw.rect(screen, WHITE, (20, 20, 200, 20), 2)
    health_text = font.render(f"Health: {player_health}%", True, WHITE)
    screen.blit(health_text, (20, 50))

    # Draw Wave Count
    wave_text = font.render(f"Wave: {wave}", True, WHITE)
    screen.blit(wave_text, (WIDTH - 150, 20))
    
    pygame.display.update()

# Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]: player_y -= player_speed
    if keys[pygame.K_s]: player_y += player_speed
    if keys[pygame.K_a]: player_x -= player_speed
    if keys[pygame.K_d]: player_x += player_speed

    # Check Collision with Memory Fragments
    for memory in memory_fragments:
        if math.hypot(memory[0] - player_x, memory[1] - player_y) < 20:
            memory_fragments.remove(memory)
            print("Memory Fragment Collected!")

    # AI Movement (Enemies)
    for enemy in enemies:
        dx, dy = player_x - enemy[0], player_y - enemy[1]
        dist = math.hypot(dx, dy)
        if dist > 0:
            enemy[0] += (dx / dist) * 2
            enemy[1] += (dy / dist) * 2

    # If an enemy touches the player, decrease health
    for enemy in enemies:
        if pygame.Rect(player_x, player_y, *player_size).colliderect(pygame.Rect(enemy[0], enemy[1], 40, 60)):
            player_health -= health_loss_per_hit
            if player_health <= 0:
                screen.fill(BLACK)
                game_over_text = font.render("You Lost! Dream Collapsed!", True, RED)
                screen.blit(game_over_text, (WIDTH//2 - 120, HEIGHT//2))
                pygame.display.update()
                pygame.time.delay(2000)
                running = False

    # If all memory fragments are collected, next wave
    if len(memory_fragments) == 0:
        wave += 1
        memory_fragments = [[random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50)] for _ in range(memory_pieces)]
        enemies.extend(spawn_enemies(2))  # Increase difficulty with more enemies
        print(f"Wave {wave} started!")

    draw_objects()
    clock.tick(30)

pygame.quit()