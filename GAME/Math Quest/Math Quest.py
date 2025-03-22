import pygame
import random

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Math Quest Game 🧮")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
BLUE = (0, 0, 200)

# Fonts
font = pygame.font.Font(None, 36)

def draw_heart(surface, x, y, size=20):
    """Draws a heart shape using Pygame"""
    top_left = (x, y - size // 3)
    top_right = (x + size, y - size // 3)
    bottom = (x + size // 2, y + size)
    left_curve_center = (x + size // 4, y - size // 2)
    right_curve_center = (x + 3 * size // 4, y - size // 2)
    
    pygame.draw.polygon(surface, RED, [top_left, top_right, bottom])
    pygame.draw.circle(surface, RED, left_curve_center, size // 3)
    pygame.draw.circle(surface, RED, right_curve_center, size // 3)

# Game Variables
score = 0
lives = 3  # 3 Health Hearts ❤️❤️❤️
input_text = ""
num1, num2 = random.randint(-10, 10), random.randint(-10, 10)
operator = random.choice(["+", "-"])
correct_answer = eval(f"{num1} {operator} {num2}")
game_over = False

# Buttons
button_rect = pygame.Rect(WIDTH // 2 - 50, HEIGHT // 2 + 50, 100, 40)

def draw_health():
    """Draws heart shapes for health representation"""
    for i in range(lives):
        draw_heart(screen, 10 + i * 35, 20)

def new_question():
    """Generates a new random math question"""
    global num1, num2, operator, correct_answer
    num1, num2 = random.randint(-10, 10), random.randint(-10, 10)
    operator = random.choice(["+", "-"])
    correct_answer = eval(f"{num1} {operator} {num2}")

def draw_ui():
    """Draws all game UI elements"""
    screen.fill(WHITE)
    draw_health()
    
    # Display question
    question_text = font.render(f"{num1} {operator} {num2} = ?", True, BLACK)
    screen.blit(question_text, (WIDTH // 2 - 50, HEIGHT // 3))
    
    # Display input box
    pygame.draw.rect(screen, BLACK, (WIDTH // 2 - 50, HEIGHT // 2, 100, 40), 2)
    input_surface = font.render(input_text, True, BLACK)
    screen.blit(input_surface, (WIDTH // 2 - 40, HEIGHT // 2 + 5))
    
    # Enter Button
    pygame.draw.rect(screen, BLUE, button_rect)
    enter_text = font.render("Enter", True, WHITE)
    screen.blit(enter_text, (button_rect.x + 20, button_rect.y + 10))
    
    # Score
    score_text = font.render(f"Score: {score}", True, GREEN)
    screen.blit(score_text, (WIDTH - 120, 30))
    
    # Game Over Message
    if game_over:
        screen.fill(WHITE)  # Clear screen
        game_over_text = font.render("Game Over!", True, RED)
        screen.blit(game_over_text, (WIDTH // 2 - 60, HEIGHT // 2 - 50))
        restart_text = font.render("Press R to Restart", True, BLACK)
        screen.blit(restart_text, (WIDTH // 2 - 90, HEIGHT // 2))
    
    pygame.display.flip()

running = True
while running:
    draw_ui()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN and not game_over:
                if input_text.strip().lstrip("-").isdigit() and int(input_text) == correct_answer:
                    score += 10
                    new_question()
                else:
                    lives -= 1
                    if lives == 0:
                        game_over = True
                input_text = ""
            elif event.key == pygame.K_BACKSPACE:
                input_text = input_text[:-1]
            elif event.key == pygame.K_r and game_over:
                score = 0
                lives = 3
                game_over = False
                new_question()
            else:
                input_text += event.unicode
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos) and not game_over:
                if input_text.strip().lstrip("-").isdigit() and int(input_text) == correct_answer:
                    score += 10
                    new_question()
                else:
                    lives -= 1
                    if lives == 0:
                        game_over = True
                input_text = ""

pygame.quit()