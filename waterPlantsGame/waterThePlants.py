import pygame
import os
import sys
#from hs import HashSet


pygame.init()
pygame.font.init()

WIDTH = 1600
HEIGHT = 800
FPS = 60
SCORE = 0



REGADERA_IMG = pygame.image.load('Assets/GardenGame/facet.png')
REGADERA = pygame.transform.scale(REGADERA_IMG, (200, 200))

REGADERA_AGUA_IMG = pygame.image.load('Assets/GardenGame/faucetWitWater.png')
REGADERA_AGUA = pygame.transform.scale(REGADERA_AGUA_IMG, (200, 200))
"""POTS: GIRASOL, POT, POT3 and the half way plant"""
GIRASOL_IMAGE = pygame.image.load('Assets/GardenGame/bucket1.png')
GIRASOL = pygame.transform.scale(GIRASOL_IMAGE, (200, 200))
HALF_PLANT_IMG = pygame.image.load('Assets/GardenGame/halfPlant1.png')
HALF_PLANT = pygame.transform.scale(HALF_PLANT_IMG, (200, 200))
GIRASOL_GROWN_IMG = pygame.image.load('Assets/GardenGame/fullFlower1.png')
GIRASOL_GROWN = pygame.transform.scale(GIRASOL_GROWN_IMG, (200, 200))

POT_IMG = pygame.image.load('Assets/GardenGame/bucket3.png')
POT = pygame.transform.scale(POT_IMG, (200, 200))

POT_FILLED_IMG = pygame.image.load('Assets/GardenGame/potFill.png')
POT_FILLED = pygame.transform.scale(POT_FILLED_IMG, (200, 200))




POT3_IMG = pygame.image.load('Assets/GardenGame/bucket2.png')
POT3 = pygame.transform.scale(POT3_IMG, (200, 200))
POT3_HALF_IMG = pygame.image.load('Assets/GardenGame/halfPlant2.png')
POT3_HALF = pygame.transform.scale(POT3_HALF_IMG, (200, 200))
POT3_FILLED_IMG = pygame.image.load('Assets/GardenGame/fullFlower2.png')
POT3_FILLED = pygame.transform.scale(POT3_FILLED_IMG, (200,200))


"""BACKGROUND"""
BACKGROUND_IMG = pygame.image.load('Assets/GardenGame/backyardBackground.png')
BACKGROUND = pygame.transform.scale(BACKGROUND_IMG, (1600, 800))


WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Water the plants")

GIRASOL_BIG = 0
POT_GROWTH = 0
POT3_GROWTH = 0
V_reg = 15
WHITE = (255, 255, 255)




def draw_window(regadera, regaderaIMG, girasolIMG, potIMG, pot3IMG):
    WINDOW.fill(WHITE)
    WINDOW.blit(BACKGROUND, (0, 0))
    WINDOW.blit(girasolIMG, (50, 100))
    WINDOW.blit(potIMG, (570, 100))
    WINDOW.blit(pot3IMG, (1300, 100))
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
    global POT3_GROWTH

    regadera = pygame.Rect(50, 200, 100, 100)
    girasol = pygame.Rect(50, 100, 200, 200)

    pot = pygame.Rect(570, 100, 200, 200)

    pot3 = pygame.Rect(1300, 100, 200, 200)
    clockAnimationWater = pygame.time.Clock()
    clock = pygame.time.Clock()
    run = True
    left = False

    time_started = pygame.time.get_ticks()
    while run:
        clock.tick(FPS)

        current_time = pygame.time.get_ticks()
        keys_pressed = pygame.key.get_pressed()
        regaderaIMG = REGADERA

        if(current_time - time_started > 35000):
            #TODO game over
            break
        if (POT_GROWTH < 3):
            potIMG = POT
        else:
            potIMG = POT_FILLED

        if (GIRASOL_BIG < 3):
            girasolIMG = GIRASOL
        elif (GIRASOL_BIG < 6 and GIRASOL_BIG >= 3):
            girasolIMG = HALF_PLANT
        else:
            girasolIMG = GIRASOL_GROWN

        if (POT3_GROWTH < 3):
            pot3IMG = POT3
        elif (POT_GROWTH < 6 and POT_GROWTH >= 3):
            pot3IMG = POT3_HALF
        else:
            pot3IMG = POT3_FILLED

        if (keys_pressed[pygame.K_x]):
            regaderaIMG = REGADERA_AGUA
            draw_window(regadera, regaderaIMG, girasolIMG, potIMG, pot3IMG)
            clockAnimationWater.tick(3)
            regaderaIMG = REGADERA
            draw_window(regadera, regaderaIMG, girasolIMG, potIMG, pot3IMG)

            if (isPlantCloseEnough(regadera, girasol)):
                GIRASOL_BIG += 1

            if (isPlantCloseEnough(regadera, pot)):
                POT_GROWTH += 1

            if (isPlantCloseEnough(regadera, pot3)):
                POT3_GROWTH += 1


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
        draw_window(regadera, regaderaIMG, girasolIMG, potIMG, pot3IMG)


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
