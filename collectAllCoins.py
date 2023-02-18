import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Create a window
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
WINDOW_SIZE = (WINDOW_WIDTH, WINDOW_HEIGHT)
window = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Collect the Yellow Circles!")

# Set up the clock
clock = pygame.time.Clock()

# Set up the colors
PURPLE = (128, 0, 128)
YELLOW = (255, 255, 0)

# Set up the player
player_radius = 20
player_pos = [WINDOW_WIDTH/2, WINDOW_HEIGHT/2]
player_speed = 5

# Set up the collectibles
collectible_radius = 10
collectible_list = []
for i in range(10):
    collectible_pos = [random.randint(0, WINDOW_WIDTH), random.randint(0, WINDOW_HEIGHT)]
    collectible_list.append(collectible_pos)

# Set up the font
font = pygame.font.Font(None, 36)

# Set up the score
score = 0
multiplier = 1
score_text = font.render("Score: " + str(score), True, PURPLE)
score_rect = score_text.get_rect()
score_rect.center = (100, 50)

# Define the level structure
level_structure = [
    {"num_collectibles": 10, "player_start": (100, 100), "collectible_positions": []},
    {"num_collectibles": 10, "player_start": (200, 200), "collectible_positions": []},
    {"num_collectibles": 10, "player_start": (300, 300), "collectible_positions": []},
    # Add more levels as necessary
]
# Set up the game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get the keyboard input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and player_pos[0] > player_radius:
        player_pos[0] -= player_speed
    if keys[pygame.K_d] and player_pos[0] < WINDOW_WIDTH - player_radius:
        player_pos[0] += player_speed
    if keys[pygame.K_w] and player_pos[1] > player_radius:
        player_pos[1] -= player_speed
    if keys[pygame.K_s] and player_pos[1] < WINDOW_HEIGHT - player_radius:
        player_pos[1] += player_speed

    # Check for collision with collectibles
    for collectible_pos in collectible_list:
        distance = math.sqrt((collectible_pos[0] - player_pos[0])**2 + (collectible_pos[1] - player_pos[1])**2)
        if distance < player_radius + collectible_radius:
            collectible_list.remove(collectible_pos)
            score += int(10 * multiplier)
            multiplier += 0.1
            if score > 999999:
                score = 999999
            score_text = font.render("Score: " + str(score), True, PURPLE)

    # Clear the screen
    window.fill((255, 255, 255))

    # Draw the collectibles
    for collectible_pos in collectible_list:
        pygame.draw.circle(window, YELLOW, collectible_pos, collectible_radius)

    # Draw the player
    pygame.draw.circle(window, PURPLE, player_pos, player_radius)

    # Draw the score
    window.blit(score_text, score_rect)

    # Update the screen
    pygame.display.update()

    # Tick the clock
    clock.tick(60)

# Quit Pygame
pygame.quit()

