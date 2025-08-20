import pygame
pygame.init()
WIDTH = 700
HEIGHT = 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill((210, 180, 140))
pygame.display.update()

geometry_dash = pygame.image.load("geometry dash.png")
marvel = pygame.image.load("marvel.png")
minecraft = pygame.image.load("minecraft.png")
clans = pygame.image.load("clans.png")


screen.blit(minecraft, (100, 50))         
screen.blit(geometry_dash, (100, 175))    
screen.blit(clans, (100, 300))     
screen.blit(marvel, (100, 425))        

font = pygame.font.SysFont("comicSansms", 30)

text4 = font.render("Clash of Clans", True, (0, 0, 0))   
text2 = font.render("Marvel Contest", True, (0, 0, 0))   
text3 = font.render("Minecraft", True, (0, 0, 0))        
text1 = font.render("Geometry Dash", True, (0, 0, 0))   

screen.blit(text4, (400, 65))    
screen.blit(text2, (400, 190))   
screen.blit(text3, (400, 315))   
screen.blit(text1, (400, 440))   

image_positions = {
    "minecraft": (100, 50),
    "geometry_dash": (100, 175),
    "clans": (100, 300),
    "marvel": (100, 425)
}

text_positions = {
    "text4": (400, 65),     
    "text2": (400, 190),   
    "text3": (400, 315),    
    "text1": (400, 440)     
}

pygame.display.update()
correct_pair = {
    "geometry_dash": "text1",
    "marvel": "text2",
    "minecraft": "text3",
    "clans": "text4"
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




                    
                    
                        

            


