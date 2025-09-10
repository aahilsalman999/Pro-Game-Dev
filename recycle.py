import pygame
import random
import time
from pygame.locals import *
pygame.init()
pygame.display.set_caption("Recycle loot!")
WIDTH = 700
HEIGHT = 600
SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))

def change_background(image):
    background = pygame.image.load(image)
    img = pygame.transform.scale(background,(WIDTH,HEIGHT))
    SCREEN.blit(img,(0,0))

class Bin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.bin = pygame.image.load("img/bin.png").convert_alpha()
        self.bin = pygame.transform.scale(self.bin,(60,80))
        self.rect = self.bin.get_rect()

class Recycable(pygame.sprite.Sprite):
    def __init__(self,img):
        super().__init__()
        self.recycable = pygame.image.load(img).convert_alpha()
        self.recycable = pygame.transform.scale(self.recycable,(60,60))
        self.rect = self.recycable.get_rect()

class Non_recycable(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.non_recycable = pygame.image.load("img/batteries.png").convert_alpha()
        self.non_recycable = pygame.transform.scale(self.non_recycable,(60,60))
        self.rect = self.non_recycable.get_rect()

images = ["img/bags.png","img/box.png","img/newspaper.png","img/pencil.png"]

#create sprite groups
items_list = pygame.sprite.Group()
battery_list = pygame.sprite.Group()
all_sprite_list = pygame.sprite.Group()

#create recycable items sprite
for sprite in range(35):
    item = Recycable(random.choice(images))
    item.rect.x = random.randrange(WIDTH - 100)
    item.rect.y = random.randrange(HEIGHT - 100)
    items_list.add(item)
    all_sprite_list.add(item)

#create non recycable items sprite
for sprite in range(20):
    item = Non_recycable()
    item.rect.x = random.randrange(WIDTH - 100)
    item.rect.y = random.randrange(HEIGHT - 100)
    battery_list.add(item)
    all_sprite_list.add(item)

#create bin sprite
bin = Bin()
all_sprite_list.add(bin)

Red = (255,0,0)
Green = (0,255,0)
Blue = (0,0,255)
White = (255,255,255)

running = True
score_count = 0
clock = pygame.time.Clock()
start_time = time.time()

time_font = pygame.font.SysFont("Comicsansms",30)
my_font = pygame.font.SysFont("Comicsansms",35)
message_font = pygame.font.SysFont("Comicsansms",50)
text = my_font.render("Score: "+ str(score_count),True,White)

while running:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    time_elapsed = time.time() - start_time
    if time_elapsed >= 50:
        if score_count > 100 and len(battery_list) >= 15:
            text = message_font.render("Congrats! You won!",True,Green)
            change_background("img/good loot.jpg")
        else:
            text = message_font.render("Unlucky! You lost!",True,Red)
            change_background("img/bad loot.png")
    else:
        change_background("img/bg.jpg")
        countdown = time_font.render("Time left:"+ str(50 - int(time_elapsed)),True,White)
        SCREEN.blit(countdown,(350,300))
    
        keys = pygame.key.get_pressed() 
        if keys[pygame.K_UP]:
            if bin.rect.y > 0:
                bin.rect.y -= 5
        if keys[pygame.K_DOWN]:
            if bin.rect.y < 530:
                bin.rect.y += 5
        if keys[pygame.K_RIGHT]:
            if bin.rect.x < 650:
                bin.rect.x += 5
        if keys[pygame.K_LEFT]:
            if bin.rect > 0:
                bin.rect.x -= 5

        item_hit_list = pygame.sprite.spritecollide(bin,items_list,True)
        battery_hit_list = pygame.sprite.spritecollide(bin,battery_list,True)
        
        for item in item_hit_list:
            score_count += 5
            text = my_font.render("Score: "+str(score_count),True,White)
        for battery in battery_hit_list:
            score_count -= 5
            text = my_font.render("Score: "+str(score_count),True,White)
        
        SCREEN.blit(text,(20,50))

        all_sprite_list.draw(SCREEN)
    pygame.display.update()
pygame.quit()


