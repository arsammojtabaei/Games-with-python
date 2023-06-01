import pygame
import time
import random

# Initialize pygame
pygame.init()

# Set the width and height of the game window
width, height = 800, 600
window = pygame.display.set_mode((width, height))

# Set the colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)

# Set the initial position and size of the snake
snake_position = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
food_position = [random.randrange(1, (width // 10)) * 10,
                 random.randrange(1, (height // 10)) * 10]
food_spawn = True

# Set the initial direction of the snake
direction = "RIGHT"
change_to = direction

# Set the speed of the snake
snake_speed = 15

# Set the game clock
clock = pygame.time.Clock()

# Set the game over flag
game_over = False


# Function to display the game over message
def display_game_over():
    font = pygame.font.Font(None, 40)
    game_over_text = font.render("Game Over", True, red)
    game_over_rect = game_over_text.get_rect()
    game_over_rect.midtop = (width / 2, height / 4)
    window.blit(game_over_text, game_over_rect)
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()


# Main game loop
while not game_over:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != "DOWN":
                change_to = "UP"
            elif event.key == pygame.K_DOWN and direction != "UP":
                change_to = "DOWN"
            elif event.key == pygame.K_LEFT and direction != "RIGHT":
                change_to = "LEFT"
            elif event.key == pygame.K_RIGHT and direction != "LEFT":
                change_to = "RIGHT"

    # Update the snake direction
    direction = change_to

    # Move the snake
    if direction == "UP":
        snake_position[1] -= 10
    elif direction == "DOWN":
        snake_position[1] += 10
    elif direction == "LEFT":
        snake_position[0] -= 10
    elif direction == "RIGHT":
        snake_position[0] += 10

    # Snake body mechanism
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == food_position[0] and snake_position[1] == food_position[1]:
        food_spawn = False
    else:
        snake_body.pop()

    if not food_spawn:
        food_position = [random.randrange(1, (width // 10)) * 10,
                         random.randrange(1, (height // 10)) * 10]
    food_spawn = True

    # Update the game window
    window.fill(black)
    for pos in snake_body:
        pygame.draw.rect(window, white, pygame.Rect(
            pos[0], pos[1], 10, 10))

    pygame.draw.rect(window, red, pygame.Rect(
        food_position[0], food_position[1], 10, 10))

    if snake_position[0] < 0 or snake_position[0] >= width or snake_position[1] < 0 or snake_position[1] >= height:
        game_over = True
        display_game_over()

    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over = True
            display_game_over()

    pygame.display.update()

    # Set the speed of the game
    clock.tick(snake_speed)

# Quit the game
pygame.quit()
