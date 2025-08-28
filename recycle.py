import pygame
import random
import time
from pygame.locals import *
pygame.init()
pygame.display.set_caption("Recycle loot!")
WIDTH = 700
HEIGHT = 600
SCREEN = pygame.display.set_mode(WIDTH,HEIGHT)

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
    