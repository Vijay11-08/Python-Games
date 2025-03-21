import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Game Constants
WIDTH, HEIGHT = 600, 600
ROWS, COLS = 10, 10  # Maze grid size
CELL_SIZE = WIDTH // COLS
WHITE, BLACK, RED, GREEN, BLUE, GRAY = (255, 255, 255), (0, 0, 0), (200, 0, 0), (0, 200, 0), (0, 0, 255), (169, 169, 169)
FONT = pygame.font.Font(None, 36)

# Player Constants
player_pos = [0, 0]
exit_pos = [ROWS - 1, COLS - 1]

# Maze Generation using DFS
def generate_maze():
    maze = [[1] * COLS for _ in range(ROWS)]
    stack = [(0, 0)]
    maze[0][0] = 0
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while stack:
        x, y = stack[-1]
        random.shuffle(directions)
        moved = False
        
        for dx, dy in directions:
            nx, ny = x + 2 * dx, y + 2 * dy
            if 0 <= nx < ROWS and 0 <= ny < COLS and maze[nx][ny] == 1:
                maze[x + dx][y + dy] = 0
                maze[nx][ny] = 0
                stack.append((nx, ny))
                moved = True
                break
        
        if not moved:
            stack.pop()
    return maze

maze = generate_maze()

# Initialize Pygame Window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Escape the Maze")
clock = pygame.time.Clock()

# Game Loop
running = True
while running:
    screen.fill(WHITE)
    
    # Draw Maze
    for row in range(ROWS):
        for col in range(COLS):
            color = BLACK if maze[row][col] == 1 else GRAY
            pygame.draw.rect(screen, color, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    
    # Draw Player & Exit
    pygame.draw.rect(screen, RED, (player_pos[1] * CELL_SIZE, player_pos[0] * CELL_SIZE, CELL_SIZE, CELL_SIZE), border_radius=8)
    pygame.draw.rect(screen, GREEN, (exit_pos[1] * CELL_SIZE, exit_pos[0] * CELL_SIZE, CELL_SIZE, CELL_SIZE), border_radius=8)
    
    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            new_pos = list(player_pos)
            if event.key == pygame.K_UP:
                new_pos[0] -= 1
            elif event.key == pygame.K_DOWN:
                new_pos[0] += 1
            elif event.key == pygame.K_LEFT:
                new_pos[1] -= 1
            elif event.key == pygame.K_RIGHT:
                new_pos[1] += 1
            
            # Move if within bounds & not a wall
            if 0 <= new_pos[0] < ROWS and 0 <= new_pos[1] < COLS and maze[new_pos[0]][new_pos[1]] == 0:
                player_pos = new_pos
            
            # Check Win Condition
            if player_pos == exit_pos:
                screen.fill(WHITE)
                text = FONT.render("Congratulations! You escaped the maze!", True, BLUE)
                screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2))
                pygame.display.update()
                pygame.time.delay(3000)
                running = False
    
    clock.tick(30)

pygame.quit()
sys.exit()