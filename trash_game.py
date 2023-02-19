import os
import pygame

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
BIN_WIDTH, BIN_HEIGHT = 150, 75 #maybe change
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
    strikes = 0
    playing = True
    has_answered = False
    grey_bin = pygame.Rect(200, 100, BIN_WIDTH, BIN_HEIGHT)
    green_bin = pygame.Rect(600, 100, BIN_WIDTH, BIN_HEIGHT)
    blue_bin = pygame.Rect(1000, 100, BIN_WIDTH, BIN_HEIGHT)
    to_sort = [('Assets/TrashGame/Compost1.png', COMPOST_KEY), ('Assets/TrashGame/Compost2.png', COMPOST_KEY), ('Assets/TrashGame/Compost3.png', COMPOST_KEY),
               ('Assets/TrashGame/Compost4.png', COMPOST_KEY), ('Assets/TrashGame/Recycle1.png', RECYCLE_KEY), ('Assets/TrashGame/Recycle2.png', RECYCLE_KEY),
               ('Assets/TrashGame/Recycle3.png', RECYCLE_KEY), ('Assets/TrashGame/Recycle4.png', RECYCLE_KEY), ('Assets/TrashGame/Recycle5.png', RECYCLE_KEY),
               ('Assets/TrashGame/Recycle6.png', RECYCLE_KEY), ('Assets/TrashGame/Trash1.png', TRASH_KEY), ('Assets/TrashGame/Trash1.png', TRASH_KEY)]
    
    clock = pygame.time.Clock()
    while playing:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        #make sure clock continues counting down? (take in time, return time??)
        for item in to_sort:
            has_answered = False
            draw_window(item[0], blue_bin, green_bin, grey_bin)
            while not has_answered:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if not event.key == item[1]:
                            strikes += 1
                        break
                if strikes >= 3:
                    break
        if strikes >= 3:
            #print out ask to continue
            os.wait(5000)
            #case for handling continue?
        else:
            win_game = True
            # playing = False


        

def draw_window(item, blue_bin, green_bin, grey_bin):
    WINDOW.blit(BACKG, (0, 0))
    WINDOW.blit(BLUE_BIN, (blue_bin.x, blue_bin.y))
    WINDOW.blit(GREY_BIN, (grey_bin.x, grey_bin.y))
    WINDOW.blit(GREEN_BIN, (green_bin.x, green_bin.y))
    WINDOW.blit(pygame.image.load(item), (800, 600))

    pygame.display.update()

def main():
    screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
    trash_game()
    pygame.display.flip()

    main()

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
