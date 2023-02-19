import os
import random
import time
import pygame
pygame.font.init()
pygame.font.Font("Assets/pixel_font.ttf", 5)

pygame.display.set_caption("Sort Trash")

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
BIN_WIDTH, BIN_HEIGHT = 150, 200 #maybe change
WINDOW = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
BACKG = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'kitchen_background.png')), (SCREEN_WIDTH, SCREEN_HEIGHT))

STRIKE_FONT = pygame.font.Font("Assets/pixel_font.ttf", 20)
USE_FONT = pygame.font.Font("Assets/pixel_font.ttf", 50)

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
        time.sleep(.2)
        if index >= len(to_sort) or strikes >= 3:
            if strikes < 3:
                win_game = True
            break
    end_window(win_game)
    return win_game

                
def check_response(keys_pressed, corr_key):
    global strikes
    if keys_pressed[corr_key]:
        return 0
    if keys_pressed[TRASH_KEY] or keys_pressed[COMPOST_KEY] or keys_pressed[RECYCLE_KEY]:
        strikes += 1
    return -1         
     

def draw_window(item, blue_bin, green_bin, grey_bin):
    global strikes
    WINDOW.blit(BACKG, (0, 0))
    WINDOW.blit(BLUE_BIN, (blue_bin.x, blue_bin.y))
    WINDOW.blit(GREY_BIN, (grey_bin.x, grey_bin.y))
    WINDOW.blit(GREEN_BIN, (green_bin.x, green_bin.y))
    WINDOW.blit(pygame.transform.scale(pygame.image.load(item), (75, 100)), (600, 500))
    strikes_text = STRIKE_FONT.render(
        "Strikes: " + str(strikes), 1, (0,0,0))
    WINDOW.blit(strikes_text, (SCREEN_WIDTH - strikes_text.get_width() - 10, 10))
    instructions = STRIKE_FONT.render(
        "Press the left arrow for trash, up for compost, right for recycling", 1, (0,0,0))
    WINDOW.blit(instructions, (SCREEN_WIDTH//2 - instructions.get_width()//2, SCREEN_HEIGHT - 30 - instructions.get_height()))

    pygame.display.update()

def end_window(winner):
    WINDOW.blit(BACKG, (0, 0))
    if winner:
        win_text = USE_FONT.render(
        "YOU WON!", 1, (0,0,0))
        #print you won!
    else:
        win_text = USE_FONT.render(
        "YOU LOST :(", 1, (0,0,0))
    WINDOW.blit(win_text, (SCREEN_WIDTH//2 - win_text.get_width()//2, SCREEN_HEIGHT//2 - win_text.get_height()//2))
    pygame.display.update()
    pygame.time.delay(3000)


def main():
    screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
    winner = trash_game()
    if winner:
        print("you won")
    else:
        print("you lost")
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
