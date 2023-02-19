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
image1 = pygame.image.load("tvMiniGame/warm_1.png")
image2 = pygame.image.load("tvMiniGame/warm_2.png")
image3 = pygame.image.load("tvMiniGame/warm_3.png")
image4 = pygame.image.load("tvMiniGame/warm_4.png")
image5 = pygame.image.load("tvMiniGame/warm_5.png")

# Create a list of the images
images = [image1, image2, image3, image4, image5]

# Set the positions of the images on the screen
image_positions = [(100, 100), (250, 100), (400, 100), (550, 100), (700, 100)]

# Shuffle the order of the images
import random
random.shuffle(images)

# Create a dictionary to store the correct positions of the images
correct_positions = [image1, image2, image3, image4, image5]

# Set the running variable to True
running = True

# Set the clock for the game
clock = pygame.time.Clock()

# Main game loop
num1 = -1
num2 = -1
while running:
    # depending on if its num 1 or 2, do diff things :")
    for event in pygame.event.get():
        if num1 != -1:
            if event.type == pygame.KEYDOWN and event.unicode.isnumeric() and len(event.unicode) == 1:
                num2 = int(event.unicode)
                images[num1 - 1], images[num2 - 1] = images[num2 - 1], images[num1 - 1]
                num1 = -1
                num2 = -1
        
        else:
            if event.type == pygame.KEYDOWN and event.unicode.isnumeric() and len(event.unicode) == 1:
                num1 = int(event.unicode)
        
        count = 0 
        
        if images == correct_positions: 
            # put a "u won!" msg here + exit button
            pygame.quit()
        


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
