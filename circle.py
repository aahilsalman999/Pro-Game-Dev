import pygame
pygame.init()
screen = pygame.display.set_mode((400,200))
red = (255,0,0)
yellow = (255,255,0)
black = (0,0,0)
screen.fill(black)

class Circle:
  def __init__(self,color,position,radius):
    self.surface = screen
    self.position = position
    self.radius = radius
    self.color = color
  
  def draw(self):
    pygame.draw.circle(self.surface,self.color,
                       self.position,self.radius)
circle_1 = Circle(red,(200,100),20)
circle_2 = Circle(yellow,(300,150),40)

circle_1.draw()
circle_2.draw()
pygame.display.update()
running = True
while running:
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         running = False
        
#quit pygame properly
pygame.quit()

       