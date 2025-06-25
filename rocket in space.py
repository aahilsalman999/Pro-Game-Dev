import pygame
pygame.init()
pygame.display.set_caption("Rocket in Space!")
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH,HEIGHT))
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("ship.png")
        self.image = pygame.transform.scale(self.image , (40,40))
        self.rect = self.image.get_rect()
    
    def update(self,pressed_key):
        if pressed_key[pygame.K_UP]:
            self.rect.move_ip(0,-5)
        elif pressed_key[pygame.K_DOWN]:
            self.rect.move_ip(0,5)
        elif pressed_key[pygame.K_RIGHT]:
            self.rect.move_ip(5,0)
        elif pressed_key[pygame.K_LEFT]:
            self.rect.move_ip(-5,0)
        
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > WIDTH:
            self.rect.right = WIDTH
        elif self.rect.top <= 0:
            self.rect.top = 0
        elif self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT

sprites = pygame.sprite.Group()

def start_game():
    player = Player()
    sprites.add(player)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)

        pressed_key = pygame.key.get_pressed()
        player.update(pressed_key)
        screen.blit(pygame.image.load("space.png"),(0,0))

        sprites.draw(screen)
        pygame.display.update()

start_game()
        

        