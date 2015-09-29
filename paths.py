import pygame

pygame.init()

window = pygame.display.set_mode((500, 400))

while True:

    pygame.draw.line(window, (255, 0, 0), (100, 200), (300, 200), 5)
    pygame.draw.line(window, (0, 255, 0), (100, 200), (200, 100), 5)
    pygame.draw.line(window, (0, 0, 255), (300, 200), (200,100), 5)
    
    pygame.display.update()
