import pygame
pygame.init()
SCREEN = pygame.display.set_mode((800,600))
Blue = (0,0,255)
pygame.display.update()

class Circle:
    def __init__(self,radius,color,width,pos):
        self.radius = radius
        self.color = color
        self.width = width
        self.pos = pos
        self.surface = SCREEN
    
    def draw(self):
        self.draw_circle = pygame.draw.circle(self.surface,self.radius,self.color,self.width,self.pos)
    
    def grow(self,in_radius):
        self.radius = self.radius + in_radius
        self.draw_circle = pygame.draw.circle(self.surface,self.radius,self.color,self.width,self.pos)

circle1 = Circle(30,Blue,30,(0,0))
while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            SCREEN.fill((255,255,255))
            circle1.draw()
            pygame.display.update()
        






