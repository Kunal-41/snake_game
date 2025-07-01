import pygame
import random

# Initialize pygame
pygame.init()

# Game window settings
WIDTH, HEIGHT = 600, 400
BLOCK_SIZE = 10  # Size of the snake and food
FPS = 15

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Set up display
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Snake settings
snake = [(100, 100)]
snake_dir = (BLOCK_SIZE, 0)

# Food settings
food = (random.randint(0, WIDTH // BLOCK_SIZE - 1) * BLOCK_SIZE,
        random.randint(0, HEIGHT // BLOCK_SIZE - 1) * BLOCK_SIZE)

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    win.fill(BLACK)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_dir != (0, BLOCK_SIZE):
                snake_dir = (0, -BLOCK_SIZE)
            elif event.key == pygame.K_DOWN and snake_dir != (0, -BLOCK_SIZE):
                snake_dir = (0, BLOCK_SIZE)
            elif event.key == pygame.K_LEFT and snake_dir != (BLOCK_SIZE, 0):
                snake_dir = (-BLOCK_SIZE, 0)
            elif event.key == pygame.K_RIGHT and snake_dir != (-BLOCK_SIZE, 0):
                snake_dir = (BLOCK_SIZE, 0)

    # Move the snake
    new_head = (snake[0][0] + snake_dir[0], snake[0][1] + snake_dir[1])
    snake.insert(0, new_head)

    # Check for collisions
    if (new_head in snake[1:] or
        new_head[0] < 0 or new_head[0] >= WIDTH or
        new_head[1] < 0 or new_head[1] >= HEIGHT):
        running = False  # Game Over

    # Check if food is eaten
    if new_head == food:
        food = (random.randint(0, WIDTH // BLOCK_SIZE - 1) * BLOCK_SIZE,
                random.randint(0, HEIGHT // BLOCK_SIZE - 1) * BLOCK_SIZE)
    else:
        snake.pop()  # Remove tail segment

    # Draw food
    pygame.draw.rect(win, RED, (food[0], food[1], BLOCK_SIZE, BLOCK_SIZE))

    # Draw snake
    for segment in snake:
        pygame.draw.rect(win, GREEN, (segment[0], segment[1], BLOCK_SIZE, BLOCK_SIZE))

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()