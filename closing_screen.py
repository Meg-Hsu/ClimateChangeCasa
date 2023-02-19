import pygame
import time

closing_image_img = pygame.image.load("Assets/closingImage.png")
closing_image = pygame.transform.scale(closing_image_img, (800, 600))


def closing_message():
    window = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Closing Image")
    draw_window(window)
    time.sleep(4)


def draw_window(window):
    window.blit(closing_image, (0, 0))
    pygame.display.update()
