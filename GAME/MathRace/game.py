import pygame
import time
from config import *
from player import Player
from ai import AI
from math_questions import generate_question

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Math Race 🚗💨")
font = pygame.font.Font(None, 40)

# Image Paths (Absolute)
TRACK_IMAGE = r"D:\PD CIE-2\GAME\MathRace\assets\track.jpg"
PLAYER_CAR_IMAGE = r"D:\PD CIE-2\GAME\MathRace\assets\car.jpg"
AI_CAR_IMAGE = r"D:\PD CIE-2\GAME\MathRace\assets\ai_car.jpg"

# Load track background
track = pygame.image.load(TRACK_IMAGE)

# Initialize player and AI racers
player = Player(50, 200, PLAYER_CAR_IMAGE)
ai = AI(50, 300, AI_CAR_IMAGE)

# Game variables
user_input = ""
question, correct_answer = generate_question()
boost = 0
game_over = False

def draw_text(text, x, y, color=WHITE):
    """Draw text on the screen."""
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

def reset_game():
    """Reset game state."""
    global user_input, question, correct_answer, boost, game_over
    player.rect.x, ai.rect.x = 50, 50
    boost = 0
    game_over = False
    user_input = ""
    question, correct_answer = generate_question()

def game_loop():
    global user_input, boost, game_over, question, correct_answer  # Add these to global variables

    running = True
    while running:
        screen.fill(BLACK)
        screen.blit(track, (0, 0))

        # Ensure a question is always available
        if not question:
            question, correct_answer = generate_question()

        # Draw cars
        player.draw(screen)
        ai.draw(screen)

        # Display math question
        draw_text(f"Q: {question}", WIDTH // 3, 50, YELLOW)
        draw_text(f"Your Answer: {user_input if user_input else '?'}", WIDTH // 3, 100, GREEN)

        # Display Finish Line
        pygame.draw.line(screen, RED, (700, 0), (700, HEIGHT), 5)

        # Check for winning condition
        if player.rect.x >= 700:
            draw_text("You Win! 🎉", WIDTH // 3, HEIGHT // 2, GREEN)
            game_over = True
        elif ai.rect.x >= 700:
            draw_text("AI Wins! 😢", WIDTH // 3, HEIGHT // 2, RED)
            game_over = True

        pygame.display.flip()

        if game_over:
            pygame.time.delay(2000)
            reset_game()

        # Event Handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if user_input == correct_answer:
                        boost = SPEED_BOOST  # Increase speed on correct answer
                    else:
                        boost = 0  # No boost on wrong answer
                    user_input = ""
                    question, correct_answer = generate_question()  # Generate new question

                elif event.key == pygame.K_BACKSPACE:
                    user_input = user_input[:-1]

                elif event.unicode.isdigit():
                    user_input += event.unicode

        # Move cars
        player.move(boost)
        ai.move()

        pygame.time.delay(50)

    pygame.quit()

# Run the game
if __name__ == "__main__":
    game_loop()
