import pygame
import socket
import threading
from player import Player
from bullet import Bullet
from config import WIDTH, HEIGHT, FPS

# Pygame Setup
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Battle Royale - Client")
clock = pygame.time.Clock()

# Network Setup
SERVER_IP = "127.0.0.1"
PORT = 5555
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER_IP, PORT))

# Game Variables
player = Player(400, 300, (0, 0, 255))
bullets = []

# Receiving Messages from Server
def receive_messages():
    while True:
        try:
            message = client.recv(1024).decode()
            print(message)
        except:
            break

threading.Thread(target=receive_messages, daemon=True).start()

# Game Loop
running = True
while running:
    screen.fill((255, 255, 255))
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            bullets.append(Bullet(player.rect.x, player.rect.y, 1))
            client.send(f"SHOT {player.rect.x},{player.rect.y}".encode())

    # Move Player
    player.move(keys)

    # Move Bullets
    for bullet in bullets:
        bullet.move()

    # Draw Elements
    player.draw(screen)
    for bullet in bullets:
        bullet.draw(screen)

    pygame.display.flip()
    client.send(f"{player.rect.x},{player.rect.y}".encode())


    clock.tick(FPS)

client.close()
pygame.quit()
