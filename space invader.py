import pygame
import os
pygame.font.init()
pygame.mixer.init()
WIDTH = 1000
HEIGHT = 700
pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Space Invader!")
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

border = pygame.Rect(WIDTH//2 - 5 , 0 , 10 , HEIGHT)

BULLET_HIT_SOUND = pygame.mixer.Sound("assets/Gun+Silencer.mp3")
BULLET_FIRE_SOUND = pygame.mixer.Sound("assets/Grenade+1.mp3")

HEALTH_FONT = pygame.font.SysFont("ComicSans",30)
WINNER_FONT = pygame.font.SysFont("ComicSans",100)

