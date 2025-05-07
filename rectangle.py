import pygame
#initialise pygame
pygame.init()

#set up display
screen = pygame.display.set_mode((600,400))
pygame.display.set_caption("Rectangle:")

#define colour
red = (255,0,0)
black = (0,0,0)
yellow = (255,255,0)
green = (0,255,0)

#fill screen with green colour
screen.fill(green)

#define a rectangle class
class Rectangle:
   def __init__(self,color,dimension):
      self.surf = screen
      self.color = color
      self.dimension = dimension
    
   def draw(self):
      pygame.draw.rect(self.surf,self.color,self.dimension)

#create rectangle object
red_rectangle = Rectangle(red,(10,10,100,200))
black_rectangle = Rectangle(black,(200,10,200,100))
yellow_rectangle = Rectangle(yellow,(10,300,200,300))    

#draw rectangles
red_rectangle.draw()
black_rectangle.draw()
yellow_rectangle.draw()

#update display
pygame.display.update()
running = True
while running:
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         running = False
        
#quit pygame properly
pygame.quit()