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
image1 = pygame.image.load("minigame/warm_1.png")
image2 = pygame.image.load("minigame/warm_2.png")
image3 = pygame.image.load("minigame/warm_3.png")
image4 = pygame.image.load("minigame/warm_4.png")
image5 = pygame.image.load("minigame/warm_5.png")

# Create a list of the images
images = [image1, image2, image3, image4, image5]

# Set the positions of the images on the screen
image_positions = [(100, 100), (250, 100), (400, 100), (550, 100), (700, 100)]

# Shuffle the order of the images
import random
random.shuffle(images)

# Create a dictionary to store the correct positions of the images
correct_positions = {image1: (100, 100), image2: (250, 100), image3: (400, 100), image4: (550, 100), image5: (700, 100)}

# Set the font for the instructions
font = pygame.font.SysFont('Arial', 30)

# Create a text surface for the instructions
text = font.render('Sort the images in the correct order', True, BLACK)

# Set the initial position of the mouse
mouse_position = None

# Set the running variable to True
running = True

# Set the clock for the game
clock = pygame.time.Clock()

# Main game loop
while running:
    # Handle events
    for event in pygame.event.get():
        # If the user clicks the close button, exit the game
        if event.type == pygame.QUIT:
            running = False
        # If the user clicks the mouse button, get the mouse position
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_position = pygame.mouse.get_pos()
        # If the user releases the mouse button, check if an image is being dragged and if it is in the correct position
        elif event.type == pygame.MOUSEBUTTONUP:
            if mouse_position is not None:
                for image in images:
                    if image.get_rect().collidepoint(mouse_position):
                        if image.get_rect().center == correct_positions[image]:
                            images.remove(image)
                            correct_positions.pop(image)
                            if len(images) == 0:
                                text = font.render('Congratulations, you sorted the images!', True, BLACK)
                            break
                        else:
                            image_position = image_positions[images.index(image)]
                            images.remove(image)
                            images.insert(0, image)
                            image_positions.remove(image_position)
                            image_positions.insert(0, image_position)
                        break

    # Clear the screen
    screen.fill(WHITE)

    # Draw the images on the screen
    for i, image in enumerate(images):
        screen.blit
