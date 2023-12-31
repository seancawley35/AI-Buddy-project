import pygame
import random
import time
from playsound import playsound

# Import the chatbot
import buddyDemoUpdate

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Define the size of the window
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480

# Create the window
pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Define the avatar
avatar = pygame.image.load("avatar.png")
avatar_rect = avatar.get_rect()
avatar_rect.centerx = WINDOW_WIDTH // 2
avatar_rect.centery = WINDOW_HEIGHT // 2

# Define the background
background = pygame.image.load("background.png")

# Create a list of colors to choose from
colors = [BLACK, WHITE, RED, GREEN, BLUE]

# Start the main loop
while True:
    # Check for events
    for event in pygame.event.get():
        # If the user quits, exit the game
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        # If the user clicks the mouse, change the avatar's color
        if event.type == pygame.MOUSEBUTTONDOWN:
            avatar_color = random.choice(colors)
            avatar.fill(avatar_color)

    # Draw the background
    screen.blit(background, (0, 0))

    # Draw the avatar
    screen.blit(avatar, avatar_rect)

    # Draw the mouth
    mouth = pygame.image.load("mouth.png")
    mouth_rect = mouth.get_rect()
    mouth_rect.centerx = avatar_rect.centerx
    mouth_rect.centery = avatar_rect.centery + avatar.get_height() // 2
    screen.blit(mouth, mouth_rect)

    # Update the display
    pygame.display.update()

    # Generate a response
    response = buddyDemoUpdate.generate_response()

    # Move the mouth
    for i in range(len(response)):
        time.sleep(0.5)
        mouth_rect.centery += 10

    # Print the response
    print(response)

    # Play the audio file
    playsound("response.mp3")
