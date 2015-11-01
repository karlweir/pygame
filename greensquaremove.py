import pygame, sys, random
import pygame.locals as GAME_GLOBALS
import pygame.event as GAME_EVENTS

pygame.init()
windowWidth = 640
windowHeight = 480
surface = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption('Pygame Shapes!')

greenSquareX = windowWidth / 2
greenSquareY = windowHeight / 2

while True:
    surface.fill((0,0,0))
    pygame.draw.rect(surface, (0,255,0), (greenSquareX, greenSquareY, 10, 10))
    greenSquareX += 1
    #greenSquareY += 1
    #pygame.draw.rect(surface, (0, 0, 255), (blueSquareX, blueSquareY, 10, 10))
    

    for event in GAME_EVENTS.get():
        if event.type == GAME_GLOBALS.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
