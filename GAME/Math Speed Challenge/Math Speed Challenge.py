import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Game Constants
WIDTH, HEIGHT = 800, 600
WHITE, BLACK, RED, GREEN, BLUE, YELLOW = (255, 255, 255), (0, 0, 0), (200, 0, 0), (0, 200, 0), (0, 0, 255), (255, 255, 0)
FONT = pygame.font.Font(None, 48)
HEART_FONT = pygame.font.Font(None, 60)

# Set up display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Math Speed Challenge")

# Game Variables
score = 0
lives = 3
base_time_limit = 10  # Base time per question
extra_time = 1  # Extra time reward for correct answer
time_limit = base_time_limit
start_time = time.time()
user_input = ""
operators = ["+", "-", "*", "/"]
num1, num2, operator = None, None, None
correct_answer = None
game_over = False

# Button setup
enter_button_rect = pygame.Rect(WIDTH//2 - 60, HEIGHT//2 + 120, 120, 50)

def generate_question():
    global num1, num2, operator, correct_answer, start_time
    num1, num2 = random.randint(1, 10), random.randint(1, 10)
    operator = random.choice(operators)
    
    if operator == "/":  # Ensure division gives a whole number
        num1 = num2 * random.randint(1, 10)
    
    correct_answer = eval(f"{num1} {operator} {num2}")  # Calculate correct answer
    if operator == "/":
        correct_answer = int(correct_answer)  # Convert to int for division
    start_time = time.time()  # Reset timer

generate_question()  # Start with a question

def draw_text(text, x, y, color=WHITE, font=FONT):
    """Draw text on the screen."""
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

def draw_hearts():
    """Draw heart symbols for lives."""
    for i in range(lives):
        pygame.draw.polygon(screen, RED, [(WIDTH - 180 + i * 50, 100), (WIDTH - 160 + i * 50, 80), (WIDTH - 140 + i * 50, 100),
                                          (WIDTH - 150 + i * 50, 120), (WIDTH - 170 + i * 50, 100)])

def game_loop():
    global user_input, score, lives, game_over, time_limit
    
    running = True
    while running:
        screen.fill(BLACK)
        elapsed_time = time.time() - start_time  # Calculate elapsed time
        
        if game_over:
            draw_text("Game Over!", WIDTH // 3, HEIGHT // 3, RED)
            draw_text(f"Final Score: {score}", WIDTH // 3, HEIGHT // 2)
            draw_text("Press R to Restart", WIDTH // 3, HEIGHT // 1.5, BLUE)
        else:
            # Display question and answer
            draw_text(f"{num1} {operator} {num2}", WIDTH // 3, HEIGHT // 4, YELLOW)  # Highlighted question
            draw_text("=", WIDTH // 2, HEIGHT // 4, BLUE)  # Distinct '=' sign
            draw_text(user_input if user_input else "?", WIDTH // 2 + 50, HEIGHT // 4, GREEN)  # User input

            # Display Timer
            remaining_time = max(0, time_limit - int(elapsed_time))
            draw_text(f"Time Left: {remaining_time}s", 50, 50, RED if remaining_time < 3 else WHITE)
            
            # Display Score and Lives
            draw_text(f"Score: {score}", WIDTH - 200, 50, GREEN)
            draw_hearts()
            
            # Draw Enter Button
            pygame.draw.rect(screen, BLUE, enter_button_rect, border_radius=10)
            draw_text("Enter", WIDTH//2 - 30, HEIGHT//2 + 130, WHITE)
            
            # Check if time is up
            if remaining_time <= 0:
                lives -= 1
                if lives == 0:
                    game_over = True
                else:
                    generate_question()
                    user_input = ""

        pygame.display.flip()

        # Event Handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.KEYDOWN:
                if game_over and event.key == pygame.K_r:
                    # Restart Game
                    game_over = False
                    score = 0
                    lives = 3
                    time_limit = base_time_limit
                    generate_question()
                    user_input = ""

                elif event.key == pygame.K_RETURN and not game_over:
                    try:
                        if int(user_input) == correct_answer:
                            score += 10
                            time_limit = min(15, time_limit + extra_time)  # Add extra time
                            generate_question()
                        else:
                            lives -= 1
                            if lives == 0:
                                game_over = True
                            else:
                                generate_question()
                    except ValueError:
                        pass  # Ignore invalid input
                    user_input = ""

                elif event.key == pygame.K_BACKSPACE:
                    user_input = user_input[:-1]

                elif event.unicode.isdigit() or event.unicode == "-":
                    user_input += event.unicode
            
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if enter_button_rect.collidepoint(event.pos) and not game_over:
                    try:
                        if int(user_input) == correct_answer:
                            score += 10
                            time_limit = min(15, time_limit + extra_time)
                            generate_question()
                        else:
                            lives -= 1
                            if lives == 0:
                                game_over = True
                            else:
                                generate_question()
                    except ValueError:
                        pass
                    user_input = ""

    pygame.quit()

# Start Game
game_loop()
