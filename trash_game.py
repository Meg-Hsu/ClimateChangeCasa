import os
import random
import time
import pygame

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
BIN_WIDTH, BIN_HEIGHT = 150, 200 #maybe change
WINDOW = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
BACKG = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'kitchen_background.png')), (SCREEN_WIDTH, SCREEN_HEIGHT))

BLUE_BIN = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'TrashGame', 'recycle.png')), (BIN_WIDTH, BIN_HEIGHT))
GREEN_BIN = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'TrashGame', 'compost.png')), (BIN_WIDTH, BIN_HEIGHT))
GREY_BIN = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'TrashGame', 'trash.png')), (BIN_WIDTH, BIN_HEIGHT))

TRASH_KEY = pygame.K_LEFT
COMPOST_KEY = pygame.K_UP
RECYCLE_KEY = pygame.K_RIGHT


def trash_game():
    win_game = False
    playing = True
    global strikes
    strikes = 0
    index = 0
    grey_bin = pygame.Rect(150, 100, BIN_WIDTH, BIN_HEIGHT)
    green_bin = pygame.Rect(550, 100, BIN_WIDTH, BIN_HEIGHT)
    blue_bin = pygame.Rect(950, 100, BIN_WIDTH, BIN_HEIGHT)
    to_sort = [('Assets/TrashGame/Compost1.png', COMPOST_KEY), ('Assets/TrashGame/Compost2.png', COMPOST_KEY), ('Assets/TrashGame/Compost3.png', COMPOST_KEY),
               ('Assets/TrashGame/Compost4.png', COMPOST_KEY), ('Assets/TrashGame/Recycle1.png', RECYCLE_KEY), ('Assets/TrashGame/Recycle2.png', RECYCLE_KEY),
               ('Assets/TrashGame/Recycle3.png', RECYCLE_KEY), ('Assets/TrashGame/Recycle4.png', RECYCLE_KEY), ('Assets/TrashGame/Recycle5.png', RECYCLE_KEY),
               ('Assets/TrashGame/Recycle6.png', RECYCLE_KEY), ('Assets/TrashGame/Trash1.png', TRASH_KEY), ('Assets/TrashGame/Trash2.png', TRASH_KEY)]
    
    random.shuffle(to_sort)

    clock = pygame.time.Clock()
    while playing:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        draw_window(to_sort[index][0], blue_bin, green_bin, grey_bin)
        keys_pressed = pygame.key.get_pressed()
        if check_response(keys_pressed, to_sort[index][1]) == 0:
            index +=1
        time.sleep(.1)
        if index >= len(to_sort) or strikes >= 3:
            if strikes < 3:
                win_game = True
            break

                
def check_response(keys_pressed, corr_key):
    global strikes
    if keys_pressed[corr_key]:
        return 0
    if keys_pressed[TRASH_KEY] or keys_pressed[COMPOST_KEY] or keys_pressed[RECYCLE_KEY]:
        strikes += 1
    return -1         
     

def draw_window(item, blue_bin, green_bin, grey_bin):
    WINDOW.blit(BACKG, (0, 0))
    WINDOW.blit(BLUE_BIN, (blue_bin.x, blue_bin.y))
    WINDOW.blit(GREY_BIN, (grey_bin.x, grey_bin.y))
    WINDOW.blit(GREEN_BIN, (green_bin.x, green_bin.y))
    WINDOW.blit(pygame.transform.scale(pygame.image.load(item), (75, 100)), (600, 600))

    pygame.display.update()

def main():
    screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
    trash_game()
    pygame.display.flip()

if __name__ == "__main__":
    main()

#while loop?
#fill background with new background
#create and position bins 
#create array of objects to be sorted (tuple?)
    #tuple is of path, bin
    #user clicks on bin 
    #check mouse position, see if correct bin otherwise take a point off
    #3 strikes youre out, ask to start game again or quit
#if items sorted correctly (<3 wrong) exit (return bool true or false?)
