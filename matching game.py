import pygame
pygame.init()
WIDTH = 700
HEIGHT = 700
screen = pygame.display.set_mode((WIDTH,HEIGHT))
screen.fill((210,180,140))
pygame.display.update()

#load images
ludo = pygame.image.load("ludo.png")
mario = pygame.image.load("mario.png")
hill = pygame.image.load("hill.png")
subway_surfers = pygame.image.load("subway surfers.png")
temple_run = pygame.image.load("temple run.png")

#blit images
screen.blit(ludo,(100,50))
screen.blit(mario,(100,175))
screen.blit(hill,(100,300))
screen.blit(subway_surfers,(100,425))
screen.blit(temple_run,(100,550))

#text setup
font = pygame.font.SysFont("comicSansms",30)
text1 = font.render("Hill Climbing",True,(0,0,0))
text2 = font.render("Temple Run",True,(0,0,0))
text3 = font.render("Ludo",True,(0,0,0))
text4 = font.render("Mario",True,(0,0,0))
text5 = font.render("Subway Surfers",True,(0,0,0))

#blit text
screen.blit(text1,(400,65))
screen.blit(text2,(400,190))
screen.blit(text3,(400,315))
screen.blit(text4,(400,440))
screen.blit(text5,(400,565))

#dictionary for image and text positions
image_positions = {
    "ludo" : (100,50),
    "mario" : (100,175),
    "hill" : (100,300),
    "subway_surfers" : (100,425),
    "temple_run" : (100,550)
}

text_positions = {
    "text1" : (400,65),
    "text2" : (400,190),
    "text3" : (400,315),
    "text4" : (400,440),
    "text5" : (400,565)
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
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            pygame.draw.circle(screen,(255,255,255),pos,10,0)
            pygame.display.update()

            if not first_click:
                first_click = pos
            else:
                pos2 = pos 
                pygame.draw.circle(screen,(255,255,255),pos2,10,0)

            #which image and text are clicked
                choosen_image = None
                choosen_text = None
                
                #check if first_click is image
                for key, (x,y) in image_positions.items():
                    rect = pygame.Rect(x,y,100,100)
                    if rect.collidepoint(first_click):
                        choosen_image = key

                for key, (x,y) in text_positions.items():
                    rect = pygame.Rect(x,y,200,50)
                    if rect.collidepoint(pos2):
                        choosen_text = key

                #if first click is on text
                for key, (x,y) in image_positions.items():
                    rect = pygame.Rect(x,y,100,100)
                    if rect.collidepoint(pos2):
                        choosen_image = key

                for key, (x,y) in text_positions.items():
                    rect = pygame.Rect(x,y,200,50)
                    if rect.collidepoint(first_click):
                        choosen_text = key
                
                #default colours
                default_colour = (255,255,255)
                if choosen_image and choosen_text:
                    if correct_pair[choosen_image] == choosen_text:
                        default_colour = (0,255,0)
                
                pygame.draw.line(screen,default_colour,first_click,pos2,5)
                pygame.display.update()
                first_click = None




                    
                    
                        

            

