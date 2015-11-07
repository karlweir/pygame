import pygame, sys, random
import pygame.locals as GAME_GLOBALS
import pygame.event as GAME_EVENTS

pygame.init()
windowWidth = 640
windowHeight = 480
surface = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption('Pygame Shapes!')

rectX = windowWidth / 2
rectY = windowHeight / 2
rectWidth = 50
rectHeight = 50

while True:
    surface.fill((0,0,0))
    pygame.draw.rect(surface, (255, 255, 0), (rectX - rectWidth / 2, rectY - rectHeight / 2, rectWidth, rectHeight))
    rectWidth += 1
    rectHeight += 1

    for event in GAME_EVENTS.get():
        if event.type == GAME_GLOBALS.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
