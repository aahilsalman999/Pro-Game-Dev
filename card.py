import pygame
import time
pygame.init()
width = 700
height = 500
SCREEN = pygame.display.set_mode((width,height))
pygame.display.set_caption("Happy Birthday!")

img1 = pygame.image.load("message2.png")
image1 = pygame.transform.scale(img1,(width,height))

run = True
while run:
    font = pygame.font.SysFont("comicsansms",35)
    text1 = font.render("Have a great day!", True , (0,0,0))
    SCREEN.fill((255,255,255))
    SCREEN.blit(image1 , (0,0))
    SCREEN.blit(text1 , (20,350))
    pygame.display.update()
    time.sleep(3)
    img2 = pygame.image.load("message4.png")
    img3 = pygame.image.load("message1.png")
    text2 = font.render("Hope all yor wishes come true!", True , (0,0,0))
    SCREEN.blit(img2 , (0,0))
    SCREEN.blit(img3 , (30,250))
    SCREEN.blit(text2 , (20,100))
    pygame.display.update()
    time.sleep(3)
    img4 = pygame.image.load("message3.png")
    text3 = font.render("Woohoo!!!!!!!!!", True , (0,0,0))
    SCREEN.blit(img4 , (0,0))
    SCREEN.blit(text3 , (20,0))

    
    pygame.display.update()
    time.sleep(3)
    run = False
