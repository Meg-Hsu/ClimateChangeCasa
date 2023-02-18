import pygame

WIDTH, HEIGHT = 1000, 600 #maybe change
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Climate Change Casa")

#WHITE = (255, 255, 255)

def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        #WIN.fill(WHITE)
        #pygame.display.update

    pygame.quit()

