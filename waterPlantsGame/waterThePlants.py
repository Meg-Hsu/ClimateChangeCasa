import pygame
import os
import sys
#from hs import HashSet


pygame.init()
pygame.font.init()

WIDTH = 1000
HEIGHT = 700
FPS = 60
SCORE = 0



REGADERA_IMG = pygame.image.load('facet.png')
REGADERA = pygame.transform.scale(REGADERA_IMG, (200, 200))

REGADERA_AGUA_IMG = pygame.image.load('faucetWitWater.png')
REGADERA_AGUA = pygame.transform.scale(REGADERA_AGUA_IMG, (200, 200))
"""POTS: GIRASOL, POT, POT3 and the half way plant"""
GIRASOL_IMAGE = pygame.image.load('maceta.png')
GIRASOL = pygame.transform.scale(GIRASOL_IMAGE, (250, 180))
GIRASOL_GROWN_IMG = pygame.image.load('grownGirasol.png')
GIRASOL_GROWN = pygame.transform.scale(GIRASOL_GROWN_IMG, (200, 200))

POT_IMG = pygame.image.load('pot.png')
POT = pygame.transform.scale(POT_IMG, (200, 250))
POT_FILLED_IMG = pygame.image.load('potFill.png')
POT_FILLED = pygame.transform.scale(POT_FILLED_IMG, (200, 250))

HALF_PLANT_IMG = pygame.image.load('halfPlant.png')
HALF_PLANT = pygame.transform.scale(HALF_PLANT_IMG, (200, 200))


POT3_IMG = pygame.image.load('pot3.png')
POT3 = pygame.transform.scale(POT3_IMG, (250, 180))


"""BACKGROUND"""
BACKGROUND_IMG = pygame.image.load('backgroundFlowers.jpeg')
BACKGROUND = pygame.transform.scale(BACKGROUND_IMG, (1000, 750))


WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Water the plants")

GIRASOL_BIG = 0
POT_GROWTH = 0
V_reg = 5
WHITE = (255, 255, 255)




def draw_window(regadera, regaderaIMG, girasolIMG, potIMG, pot3IMG):
    WINDOW.fill(WHITE)
    WINDOW.blit(BACKGROUND, (0, 0))
    WINDOW.blit(girasolIMG, (50, 100))
    WINDOW.blit(potIMG, (350, 100))
    WINDOW.blit(pot3IMG, (700, 100))
    WINDOW.blit(regaderaIMG, (regadera.x, regadera.y))
    pygame.display.update()


def isPlantCloseEnough(hose, plant):

    if (hose.x - plant.x < 250 and hose.y - plant.y < 50 and hose.x - plant.x > 50 and hose.y - plant.y > -50):
        return True
    else:
        return False


def doWaterThePlantsGame():
    global GIRASOL_BIG
    global POT_GROWTH
    regadera = pygame.Rect(50, 200, 100, 100)
    girasol = pygame.Rect(50, 100, 200, 200)

    pot = pygame.Rect(350, 100, 200, 250)
    clockAnimationWater = pygame.time.Clock()
    clock = pygame.time.Clock()
    run = True

    time_started = pygame.time.get_ticks()
    while run:
        clock.tick(FPS)

        current_time = pygame.time.get_ticks()
        keys_pressed = pygame.key.get_pressed()
        regaderaIMG = REGADERA

        if(current_time - time_started > 35000):
            #TODO game over
            break
        if (POT_GROWTH < 5):
            potIMG = POT
        else:
            potIMG = POT_FILLED

        if (GIRASOL_BIG < 3):
            girasolIMG = GIRASOL
        elif (GIRASOL_BIG < 10 and GIRASOL_BIG > 3):
            girasolIMG = HALF_PLANT
        else:
            girasolIMG = GIRASOL_GROWN
        if (keys_pressed[pygame.K_x]):
            regaderaIMG = REGADERA_AGUA
            draw_window(regadera, regaderaIMG, girasolIMG, potIMG, POT3)
            clockAnimationWater.tick(3)
            regaderaIMG = REGADERA
            draw_window(regadera, regaderaIMG, girasolIMG, potIMG, POT3)

            if (isPlantCloseEnough(regadera, girasol)):
                GIRASOL_BIG += 1

            if (isPlantCloseEnough(regadera, pot)):
                POT_GROWTH += 1


        draw_window(regadera, regaderaIMG, girasolIMG, potIMG, POT3)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        if (keys_pressed[pygame.K_LEFT]):
            regadera.x -= V_reg
        if (keys_pressed[pygame.K_RIGHT]):
            regadera.x += V_reg
        if (keys_pressed[pygame.K_UP]):
            regadera.y -= V_reg
        if (keys_pressed[pygame.K_DOWN]):
            regadera.y += V_reg



#doGame()

"""
IDEA when it gets close to the a letter pops up and you have to click it a lot
the plant grows you have a 30 sec timer to water 10 plants, every click its like 
3 percent of completion so you have to click it 33 times and it changes letter

things to finish:
- sprites
- size of watering
- moving of sprites
- points needed to win - if you get 5 plants you win wtv points if you do 10 you win double
- adding more plants
- background
"""
