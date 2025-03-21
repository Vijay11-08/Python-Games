import pygame
import random
import math

# Initialize pygame
pygame.init()
global player_health
# Game Constants
WIDTH, HEIGHT = 800, 600
WHITE, BLACK, RED, GREEN = (255, 255, 255), (0, 0, 0), (200, 0, 0), (0, 200, 0)

# Player Properties
player_size = 40
player_speed = 5
player_pos = [WIDTH // 2, HEIGHT // 2]
player_health = 100  # Health starts at 100

# Zombie Properties
zombie_size = 40
zombies = []
zombie_speed = 1.5
wave_count = 1
damage_per_hit = 10  # Health loss per zombie hit

# Bullet Properties
bullets = []
bullet_speed = 8
bullet_size = 8

# Game Setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Zombie Survival Shooter")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)

# Spawn Zombies
def spawn_zombies():
    global wave_count
    for _ in range(wave_count * 3):  # More zombies per wave
        side = random.choice(["left", "right", "top", "bottom"])
        if side == "left":
            x, y = 0, random.randint(0, HEIGHT)
        elif side == "right":
            x, y = WIDTH, random.randint(0, HEIGHT)
        elif side == "top":
            x, y = random.randint(0, WIDTH), 0
        else:
            x, y = random.randint(0, WIDTH), HEIGHT
        zombies.append([x, y])

# Fire Bullet
def fire_bullet(target_x, target_y):
    dx = target_x - player_pos[0]
    dy = target_y - player_pos[1]
    angle = math.atan2(dy, dx)
    bullets.append([player_pos[0], player_pos[1], angle])

# Game Loop
running = True
spawn_zombies()

while running:
    screen.fill(BLACK)

    # Handle Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            fire_bullet(*pygame.mouse.get_pos())

    # Player Movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]: player_pos[1] -= player_speed
    if keys[pygame.K_s]: player_pos[1] += player_speed
    if keys[pygame.K_a]: player_pos[0] -= player_speed
    if keys[pygame.K_d]: player_pos[0] += player_speed

    # Keep player inside the screen
    player_pos[0] = max(0, min(WIDTH - player_size, player_pos[0]))
    player_pos[1] = max(0, min(HEIGHT - player_size, player_pos[1]))

    # Update Zombies
      # Declare global at the beginning
    new_zombies = []
    for zombie in zombies:
        dx = player_pos[0] - zombie[0]
        dy = player_pos[1] - zombie[1]
        distance = math.sqrt(dx**2 + dy**2)
        if distance != 0:
            zombie[0] += (dx / distance) * zombie_speed
            zombie[1] += (dy / distance) * zombie_speed
        
        # Check Collision with Player
        if abs(zombie[0] - player_pos[0]) < player_size and abs(zombie[1] - player_pos[1]) < player_size:
            player_health = max(0, player_health - damage_per_hit)  # Prevent negative health
            continue  # Remove zombie after damage

        new_zombies.append(zombie)
    zombies = new_zombies

    # Update Bullets
    new_bullets = []
    for bullet in bullets:
        bullet[0] += math.cos(bullet[2]) * bullet_speed
        bullet[1] += math.sin(bullet[2]) * bullet_speed
        if 0 <= bullet[0] <= WIDTH and 0 <= bullet[1] <= HEIGHT:
            new_bullets.append(bullet)
    bullets = new_bullets

    # Check Bullet Collisions
    new_zombies = []
    for zombie in zombies:
        hit = False
        for bullet in bullets:
            if abs(zombie[0] - bullet[0]) < zombie_size and abs(zombie[1] - bullet[1]) < zombie_size:
                hit = True
                bullets.remove(bullet)
                break
        if not hit:
            new_zombies.append(zombie)
    zombies = new_zombies

    # Check if all zombies are defeated (Next Wave)
    if not zombies:
        wave_count += 1
        spawn_zombies()

    # Draw Player
    pygame.draw.rect(screen, GREEN, (*player_pos, player_size, player_size))

    # Draw Zombies
    for zombie in zombies:
        pygame.draw.rect(screen, RED, (*zombie, zombie_size, zombie_size))

    # Draw Bullets
    for bullet in bullets:
        pygame.draw.circle(screen, WHITE, (int(bullet[0]), int(bullet[1])), bullet_size)

    # Draw Health Bar
    pygame.draw.rect(screen, RED, (10, 10, 200, 20))  # Background bar
    pygame.draw.rect(screen, GREEN, (10, 10, max(0, 2 * player_health), 20))  # Prevent negative width

    # Display Wave & Health
    wave_text = font.render(f"Wave: {wave_count}", True, WHITE)
    screen.blit(wave_text, (10, 40))
    health_text = font.render(f"Health: {player_health}", True, WHITE)
    screen.blit(health_text, (WIDTH - 150, 10))

    # Check Game Over
    if player_health <= 0:
        screen.fill(BLACK)
        game_over_text = font.render("GAME OVER!", True, RED)
        screen.blit(game_over_text, (WIDTH // 2 - 100, HEIGHT // 2))
        pygame.display.update()
        pygame.time.delay(2000)
        running = False  # Exit game loop

    pygame.display.update()
    clock.tick(30)

pygame.quit()
