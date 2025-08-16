import pygame
pygame.init()
WIDTH = 700
HEIGHT = 700
screen = pygame.display.set_mode(WIDTH,HEIGHT)
screen.fill((0,0,0))
pygame.display.update()

#load images
ludo = pygame.image.load("ludo.png")
mario = pygame.image.load("mario.png")
hill = pygame.image.load("hill.png")
subway_surfers = pygame.image.load("subway surfers.png")
temple_run = pygame.image.load("temple run.png")

#blit images
screen.blit(ludo,(200,50))
screen.blit(mario,(200,75))
screen.blit(hill,(200,100))
screen.blit(subway_surfers,(200,125))
screen.blit(temple_run,(200,150))

#text setup
font = pygame.font.SysFont("comicSansms",30)
text1 = font.render("hill climbing",True,(0,0,0))
text2 = font.render("temple run",True,(0,0,0))
text3 = font.render("ludo",True,(0,0,0))
text4 = font.render("mario",True,(0,0,0))
text5 = font.render("subway surfers",True,(0,0,0))

#blit text
screen.blit(text1,(500,50))
screen.blit(text2,(500,75))
screen.blit(text3,(500,100))
screen.blit(text4,(500,125))
screen.blit(text5,(500,150))

#dictionary for image and text positions
image_positions = {
    "ludo" : (200,50),
    "mario" : (200,75),
    "hill" : (200,100),
    "subway_surfers" : (200,125),
    "temple_run" : (200,150)
}

text_positions = {
    "text1" : (500,50),
    "text2" : (500,75),
    "text3" : (500,100),
    "text4" : (500,125),
    "text5" : (500,150)
}

pygame.display.update()

#dictionary for correct image with correct text 
correct_pair = {
    "ludo" : "text3",
    "mario" : "text4",
    "hill" : "text1",
    "subway_surfers" : "text5",
    "temple_run" : "text2"
}

first_click = None
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running == False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            pygame.draw.circle(screen,(128,0,128),pos,10,0)
            pygame.display.update()

            if not first_click:
                first_click = pos
            else:
                pos2 = pos
                pygame.draw.circle(screen,(128,0,128),pos,10,0)
                       

        

