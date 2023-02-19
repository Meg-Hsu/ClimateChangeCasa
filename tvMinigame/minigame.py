import pygame
import random
pygame.font.init()
pygame.font.Font("Assets/pixel_font.ttf", 5)

# rgb colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

pygame.init()

# Set the width and height of the screen (adjust to your preference)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

INSTRUCTION_FONT = pygame.font.Font("Assets/pixel_font.ttf", 20)

# Set the caption of the window
pygame.display.set_caption("Image Sorting")

# Load the five images
image1 = pygame.image.load("tvMiniGame/warm_1.png")
image2 = pygame.image.load("tvMiniGame/warm_2.png")
image3 = pygame.image.load("tvMiniGame/warm_3.png")
image4 = pygame.image.load("tvMiniGame/warm_4.png")
image5 = pygame.image.load("tvMiniGame/warm_5.png")

# Create a list of the images

def puzzle():

    images = [image1, image2, image3, image4, image5]

    # Set the positions of the images on the screen
    image_positions = [(100, 200), (250, 200), (400, 200), (550, 200), (700, 200)]

    # Shuffle the order of the images
    random.shuffle(images)

    # Create a list to store the correct positions of the images
    correct_positions = [image1, image2, image3, image4, image5]

    # Set the running variable to True
    running = True

    # Set the clock for the game
    clock = pygame.time.Clock()

    # Main game loop
    num1 = -1
    num2 = -1
    while running:
        instructions = INSTRUCTION_FONT.render(
            "Each square corresponds to a number from the leftmost square (1) to the rightmost square (5). Type in two numbers to swap the positions of the squares to sort the colors in order.", 1, (0,0,0))
        screen.blit(instructions, (SCREEN_WIDTH//2 - instructions.get_width()//2, SCREEN_HEIGHT - 30 - instructions.get_height()))

        # depending on if its num 1 or 2, do diff things :")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

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
                print("you won")
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


def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    puzzle()
    pygame.display.flip()

if __name__ == "__main__":
    main()
