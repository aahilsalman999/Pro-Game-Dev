import pygame
pygame.init()
SCREEN = pygame.display.set_mode((800,600))
Blue = (0,0,255)
pygame.display.update()

class Circle:
    def __init__(self,color,pos,radius,width):
        self.radius = radius
        self.color = color
        self.width = width
        self.pos = pos
        self.surface = SCREEN
    
    def draw(self):
        self.draw_circle = pygame.draw.circle(self.surface,self.color,self.pos,self.radius,self.width)
    
    def grow(self,in_radius):
        self.radius = self.radius + in_radius
        self.draw_circle = pygame.draw.circle(self.surface,self.color,self.pos,self.radius,self.width)

circle1 = Circle(Blue,(400,300),30,0)
while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            SCREEN.fill((255,255,255))
            circle1.draw()
            pygame.display.update()
        elif event.type == pygame.MOUSEBUTTONUP:
            SCREEN.fill((255,255,255))
            circle1.grow(20)
            pygame.display.update()
            





