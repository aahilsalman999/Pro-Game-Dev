import pygame
pygame.init()
width = 700
height = 500
SCREEN = pygame.display.set_mode((width,height))
pygame.display.set_caption("Bulb simulator")
bulb_off = pygame.image.load("bulb2.png")
SCREEN.blit(bulb_off , (0,0))
run = True
while run:
    event = pygame.event.poll()
    if event.type == pygame.MOUSEBUTTONDOWN:
            bulb_on = pygame.image.load("bulb1.png")
            SCREEN.blit(bulb_on , (0,0))
            pygame.display.update()
    elif event.type == pygame.MOUSEBUTTONUP:
            bulb_off = pygame.image.load("bulb2.png")
            SCREEN.blit(bulb_off , (0,0))
            pygame.display.update()