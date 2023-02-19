import os
import pygame

SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 800
BIN_WIDTH, BIN_HEIGHT = 200, 150 #maybe change
WINDOW = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
BACKG = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'kitchen_background.png')), (SCREEN_WIDTH, SCREEN_HEIGHT))

BLUE_BIN = pygame.image.load(
    os.path.join('Assets', 'TrashGame', 'recycle.png'))
GREEN_BIN = pygame.image.load(
    os.path.join('Assets', 'TrashGame', 'recycle.png'))
GREY_BIN = pygame.image.load(
    os.path.join('Assets', 'TrashGame', 'recycle.png'))

def trash_game():
    win_game = False
    strikes = 3
    playing = True
    tup_count = 0
    grey_bin = pygame.Rect(400, 100, BIN_WIDTH, BIN_HEIGHT)
    green_bin = pygame.Rect(800, 100, BIN_WIDTH, BIN_HEIGHT)
    blue_bin = pygame.Rect(1200, 100, BIN_WIDTH, BIN_HEIGHT)
    while playing:
        #make sure clock continues counting down? (take in time, return time??)
        draw_window()

        

def draw_window(blue_bin, green_bin, grey_bin):
    WINDOW.blit(BACKG, (0, 0))
    WINDOW.blit(BLUE_BIN, (blue_bin.x, blue_bin.y))
    WINDOW.blit(GREY_BIN, (grey_bin.x, grey_bin.y))
    WINDOW.blit(GREEN_BIN, (green_bin.x, green_bin.y))

    pygame.display.update()

#while loop?
#fill background with new background
#create and position bins 
#create array of objects to be sorted (tuple?)
    #tuple is of path, bin
    #user clicks on bin 
    #check mouse position, see if correct bin otherwise take a point off
    #3 strikes youre out, ask to start game again or quit
#if items sorted correctly (<3 wrong) exit (return bool true or false?)
