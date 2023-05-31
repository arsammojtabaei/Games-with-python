import pygame
import random

# Initialize pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Memory Game")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (150, 150, 150)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Game settings
ROWS = 4
COLS = 4
CARD_WIDTH = 100
CARD_HEIGHT = 100
GAP = 10

# Load card images
card_images = []
for i in range(1, (ROWS * COLS) // 2 + 1):
    image = pygame.image.load(f"card{i}.png")
    image = pygame.transform.scale(image, (CARD_WIDTH, CARD_HEIGHT))
    card_images.append(image)

# Duplicate card images
card_images *= 2

# Shuffle the card images
random.shuffle(card_images)

# Create cards
cards = []
for row in range(ROWS):
    for col in range(COLS):
        x = col * (CARD_WIDTH + GAP) + GAP
        y = row * (CARD_HEIGHT + GAP) + GAP
        card = pygame.Rect(x, y, CARD_WIDTH, CARD_HEIGHT)
        cards.append((card, card_images.pop()))

# Game variables
flipped = []
matched = []
score = 0

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if len(flipped) < 2:
                pos = pygame.mouse.get_pos()
                for i, (card, image) in enumerate(cards):
                    if card.collidepoint(pos) and i not in flipped and i not in matched:
                        flipped.append(i)

    # Update game logic
    if len(flipped) == 2:
        idx1, idx2 = flipped
        if cards[idx1][1] == cards[idx2][1]:
            matched.extend([idx1, idx2])
            score += 1
        flipped = []

    # Draw the game
    SCREEN.fill(BLACK)

    for i, (card, image) in enumerate(cards):
        if i in matched:
            pygame.draw.rect(SCREEN, GRAY, card)
        else:
            pygame.draw.rect(SCREEN, WHITE, card)

        if i in flipped or i in matched:
            SCREEN.blit(image, card)

    pygame.display.flip()

    # Check for game over
    if len(matched) == len(cards):
        font = pygame.font.Font(None, 36)
        text = font.render("Game Over! Score: {}".format(score), True, RED)
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        SCREEN.blit(text, text_rect)
        pygame.display.flip()
        pygame.time.wait(3000)
        running = False

# Quit the game
pygame.quit()
