import pygame, sys, random
import pygame.locals as GAME_GLOBALS
import pygame.event as GAME_EVENTS

pygame.init()
windowWidth = 640
windowHeight = 480
surface = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption('Pygame Shapes!')

squaresRed = random.randint(0,255)
squaresBlue = random.randint(0,255)
squaresGreen = random.randint(0,255)

while True:
    surface.fill((0,0,0))
    pygame.draw.rect(surface, (squaresRed, squaresGreen, squaresBlue), (0, 0, windowWidth, windowHeight))

    if squaresRed <= 0:
        squaresRed = random.randint(0, 255)
    else:
        squaresRed -= 0.1
    if squaresGreen <= 0:
        squaresGreen = random.randint(0, 255)
    else:
        squaresGreen -= 0.1
    if squaresBlue <= 0:
        squaresBlue = random.randint(0, 255)
    else:
        squaresBlue -= 0.1

    for event in GAME_EVENTS.get():
        if event.type == GAME_GLOBALS.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
