import pygame, sys
from pygame.locals import *
import random

pygame.init()

FPS = 60 # frames per second setting
fpsClock = pygame.time.Clock()
screenWidth = 700
screenHeight = 400

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
ORANGE = (255, 83, 13)
WARMORANGE = (232, 44, 23)
RED = (255, 0, 0)
WARMPINK = (232, 12, 122)
PINK = (255, 13, 255)

colours = [ORANGE, WARMORANGE, RED, WARMPINK, PINK, WHITE]

# set up the window
DISPLAYSURF = pygame.display.set_mode((screenWidth, screenHeight), 0, 32)
pygame.display.set_caption('Animating Circles')

growSpeed = 0.5
circleRadius = 0
maxCircleRadius = 120
circlex = random.randrange(screenWidth)
circley = random.randrange(screenHeight)

circleColour = colours[random.randrange((len(colours) -1))]

while True: # the main loop
    DISPLAYSURF.fill(BLACK)
    pygame.draw.circle(DISPLAYSURF, circleColour, (circlex, circley), int(circleRadius), 0)
    circleRadius += growSpeed
    if circleRadius > maxCircleRadius:
        circleRadius = 0
        circlex = random.randint(0, 700)
        circley = random.randint(0, 400)
        circleColour = colours[random.randrange((len(colours) -1))]
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(FPS)
            
