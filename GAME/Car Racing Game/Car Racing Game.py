import pygame
import random
import math

# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🏎️ Car Racing Game")

# Colors
WHITE, BLACK, RED, GREEN, BLUE, YELLOW, GRAY = (255, 255, 255), (0, 0, 0), (200, 0, 0), (0, 200, 0), (0, 0, 200), (255, 255, 0), (100, 100, 100)

# Game properties
player_size = (50, 30)
player_speed = 4
boost_speed = 7
health = 100
race_time = 60  # Race duration in seconds
start_time = pygame.time.get_ticks()

# AI Opponents
ai_speed = 3
ai_cars = [[random.randint(100, WIDTH - 100), random.randint(100, HEIGHT - 300)] for _ in range(2)]

# Boosts, Obstacles & Track Borders
boosts = [[random.randint(100, WIDTH - 100), random.randint(100, HEIGHT - 100)] for _ in range(3)]
obstacles = [[random.randint(100, WIDTH - 100), random.randint(100, HEIGHT - 100)] for _ in range(4)]
track_borders = [(50, 50, WIDTH - 100, HEIGHT - 100)]  # Outer track borders

# Winning Zone
finish_line = (WIDTH // 2 - 50, 50, 100, 20)

# Player Position
player_x, player_y = WIDTH // 2, HEIGHT - 80
player_velocity = player_speed

# Clock & Font
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)

def draw_objects():
    screen.fill(GRAY)
    
    # Draw track borders
    for border in track_borders:
        pygame.draw.rect(screen, BLACK, border, 5)
    
    # Draw finish line
    pygame.draw.rect(screen, YELLOW, finish_line)
    finish_text = font.render("🏁 FINISH 🏁", True, BLACK)
    screen.blit(finish_text, (finish_line[0] + 10, finish_line[1] - 30))
    
    # Draw player
    pygame.draw.rect(screen, GREEN, (player_x, player_y, *player_size))
    
    # Draw AI cars
    for ai in ai_cars:
        pygame.draw.rect(screen, RED, (ai[0], ai[1], *player_size))
    
    # Draw Boosts
    for boost in boosts:
        pygame.draw.circle(screen, BLUE, boost, 10)
    
    # Draw Obstacles
    for obstacle in obstacles:
        pygame.draw.rect(screen, WHITE, (*obstacle, 30, 30))
    
    # Draw Health Bar
    pygame.draw.rect(screen, RED, (20, 20, health * 2, 20))
    pygame.draw.rect(screen, WHITE, (20, 20, 200, 20), 2)
    health_text = font.render(f"Health: {health}%", True, WHITE)
    screen.blit(health_text, (20, 50))
    
    # Draw Time Left
    elapsed_time = (pygame.time.get_ticks() - start_time) // 1000
    remaining_time = max(0, race_time - elapsed_time)
    time_text = font.render(f"Time Left: {remaining_time}s", True, WHITE)
    screen.blit(time_text, (WIDTH - 200, 20))
    
    pygame.display.update()

# Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] or keys[pygame.K_UP]: player_y -= player_velocity
    if keys[pygame.K_s] or keys[pygame.K_DOWN]: player_y += player_velocity
    if keys[pygame.K_a] or keys[pygame.K_LEFT]: player_x -= player_velocity
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]: player_x += player_velocity
    
    # Collision with Boosts
    for boost in boosts:
        if math.hypot(boost[0] - player_x, boost[1] - player_y) < 20:
            player_velocity = boost_speed  # Speed Boost
            boosts.remove(boost)  # Remove boost after pickup
    
    # Collision with Obstacles
    for obstacle in obstacles:
        if pygame.Rect(player_x, player_y, *player_size).colliderect(pygame.Rect(*obstacle, 30, 30)):
            health -= 10  # Reduce health on collision
            obstacles.remove(obstacle)
    
    # AI movement (tracking player)
    for ai in ai_cars:
        dx, dy = player_x - ai[0], player_y - ai[1]
        dist = math.hypot(dx, dy)
        if dist > 0:
            ai[0] += (dx / dist) * ai_speed
            ai[1] += (dy / dist) * ai_speed
    
    # Check Winning Condition
    if pygame.Rect(player_x, player_y, *player_size).colliderect(pygame.Rect(*finish_line)):
        screen.fill(BLACK)
        win_text = font.render("🏆 You Win! 🏆", True, GREEN)
        screen.blit(win_text, (WIDTH//2 - 60, HEIGHT//2 - 20))
        pygame.display.update()
        pygame.time.delay(2000)
        running = False
    
    # Game Over Condition
    if health <= 0 or (pygame.time.get_ticks() - start_time) // 1000 >= race_time:
        screen.fill(BLACK)
        game_over_text = font.render("💀 GAME OVER 💀", True, RED)
        screen.blit(game_over_text, (WIDTH//2 - 80, HEIGHT//2 - 20))
        pygame.display.update()
        pygame.time.delay(2000)
        running = False
    
    draw_objects()
    clock.tick(30)

pygame.quit()