import pygame

# Define the colors we will use in RGB format
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Initialize Pygame
pygame.init()

# Set the width and height of the screen (adjust to your preference)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Set the caption of the window
pygame.display.set_caption("Image Sorting")

# Load the five images
image1 = pygame.image.load("warm_1.png")
image2 = pygame.image.load("warm_2.png")
image3 = pygame.image.load("warm_3.png")
image4 = pygame.image.load("warm_4.png")
image5 = pygame.image.load("warm_5.png")

# Create a list of the images
images = [image1, image2, image3, image4, image5]

# Set the positions of the images on the screen
image_positions = [(100, 100), (250, 100), (400, 100), (550, 100), (700, 100)]

# Shuffle the order of the images
import random
random.shuffle(images)

# Create a dictionary to store the correct positions of the images
correct_positions = {image1: (100, 100), image2: (250, 100), image3: (400, 100), image4: (550, 100), image5: (700, 100)}

# Set the running variable to True
running = True

# Set the clock for the game
clock = pygame.time.Clock()

# Main game loop
while running:

    # Handle events
    for event in pygame.event.get():
        # If the user clicks the close button, exit the loop and close the window
        if event.type == pygame.QUIT:
            running = False

        # If the user types two numbers, swap the two corresponding images
        elif event.type == pygame.KEYDOWN and event.unicode.isnumeric() and len(event.unicode) == 1:
            num = int(event.unicode)
            if num >= 1 and num <= 5:
                if num - 1 < len(images) - 1:
                    images[num - 1], images[num] = images[num], images[num - 1]

    # Clear the screen
    screen.fill(WHITE)

    # Draw the images on the screen
    for i in range(len(images)):
        screen.blit(images[i], image_positions[i])

    # Update the screen
    pygame.display.flip()

    # Limit the frame rate to 60 FPS
    clock.tick(60)

# Quit Pygame
pygame.quit()
