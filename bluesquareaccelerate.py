import pygame, sys, random
import pygame.locals as GAME_GLOBALS
import pygame.event as GAME_EVENTS

pygame.init()
windowWidth = 640
windowHeight = 480
surface = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption('Pygame Shapes!')

blueSquareX = 0.0
blueSquareY = 0.0
blueSquareVX = 8
blueSquareVY = 1

while True:
    surface.fill((0,0,0))
    pygame.draw.rect(surface, (0, 0, 255), (blueSquareX, blueSquareY, 10, 10))
    blueSquareX += blueSquareVX
    blueSquareY += blueSquareVY
    blueSquareVX -= 0.1
    #blueSquareVY += 0.1

    for event in GAME_EVENTS.get():
        if event.type == GAME_GLOBALS.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
