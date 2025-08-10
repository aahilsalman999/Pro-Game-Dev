import pygame
import os
pygame.font.init()
pygame.mixer.init()
WIDTH = 1000
HEIGHT = 700
wind = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Space Invader!")

RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)

BORDER = pygame.Rect(WIDTH//2 - 5 , 0 , 10 , HEIGHT)

BULLET_HIT_SOUND = pygame.mixer.Sound("assets/Gun+Silencer.mp3")
BULLET_FIRE_SOUND = pygame.mixer.Sound("assets/Grenade+1.mp3")

HEALTH_FONT = pygame.font.SysFont("ComicSans",30)
WINNER_FONT = pygame.font.SysFont("ComicSans",100)

FPS = 60
VEL = 5
BULLET_VEL = 10
MAX_BULLETS = 3
SPACE_SHIP_WIDTH , SPACE_SHIP_HEIGHT = 120,100

#custom event identifier triggered when a ship is hit
YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 1

#load and transform images
YELLOW_SHIP = pygame.image.load(os.path.join("assets","rocket1.png"))
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SHIP,
                                                                  (SPACE_SHIP_WIDTH , SPACE_SHIP_HEIGHT)),90)
RED_SHIP = pygame.image.load(os.path.join("assets","rocket2.png"))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_SHIP,
                                                               (SPACE_SHIP_WIDTH , SPACE_SHIP_HEIGHT)),270)
SPACE = pygame.transform.scale(pygame.image.load(os.path.join("assets","space1.png")),(WIDTH,HEIGHT))

def draw_window(red,yellow,red_bullet,yellow_bullet,red_health,yellow_health):
    wind.blit(SPACE,(0,0))
    pygame.draw.rect(wind,BLUE,BORDER)

    red_health_text = HEALTH_FONT.render("Health: "+str(red_health),1,RED)
    yellow_health_text = HEALTH_FONT.render("Health: "+str(yellow_health),1,YELLOW)
    
    wind.blit(red_health_text , (WIDTH - red_health_text.get_width() - 10 , 10))
    wind.blit(yellow_health_text , (10 , 10))

    wind.blit(YELLOW_SPACESHIP,(yellow.x , yellow.y))
    wind.blit(RED_SPACESHIP,(red.x , red.y))
    
    for bullet in red_bullet:
        pygame.draw.rect(wind,RED,bullet)

    for bullet in yellow_bullet:
        pygame.draw.rect(wind,YELLOW,bullet)
    
    pygame.display.update()

def yellow_movement(key_pressed,yellow):
    if key_pressed[pygame.K_a] and yellow.x - VEL > 0:
        yellow.x -= VEL
    if key_pressed[pygame.K_d] and yellow.x + VEL + yellow.width < BORDER.x:
        yellow.x += VEL
    if key_pressed[pygame.K_w] and yellow.y - VEL > 0:
        yellow.y -= VEL
    if key_pressed[pygame.K_s] and yellow.y + VEL + yellow.height < HEIGHT - 15:
        yellow.y += VEL

def red_movement(key_pressed,red):
    if key_pressed[pygame.K_LEFT] and red.x - VEL > BORDER.x + BORDER.width:
        red.x -= VEL
    if key_pressed[pygame.K_RIGHT] and red.x + VEL + red.width < WIDTH:
        red.x += VEL
    if key_pressed[pygame.K_UP] and red.y - VEL > 0:
        red.y -= VEL
    if key_pressed[pygame.K_DOWN] and red.y + VEL + red.height < HEIGHT - 15:
        red.y += VEL

def handle_bullet(yellow_bullet,red_bullet,yellow,red):
    for bullet in yellow_bullet:
        bullet.x += BULLET_VEL
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullet.remove(bullet)
        elif bullet.x > WIDTH:
            yellow_bullet.remove(bullet)
    
    for bullet in red_bullet:
        bullet.x -= BULLET_VEL
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bullet.remove(bullet)
        elif bullet.x > WIDTH:
            red_bullet.remove(bullet)

def draw_winner(text):
    draw_text = WINNER_FONT.render(text,1,GREEN)
    wind.blit(draw_text,(WIDTH/2 - draw_text.get_width()/2 , HEIGHT/2 - draw_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(5000)

def main():
    red = pygame.Rect(800,300 , SPACE_SHIP_WIDTH , SPACE_SHIP_HEIGHT)
    yellow = pygame.Rect(200,300 , SPACE_SHIP_WIDTH , SPACE_SHIP_HEIGHT)
    
    red_bullets = []
    yellow_bullets = []

    red_health = 10
    yellow_health = 10

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(yellow_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(yellow.x + yellow.width , yellow.y + yellow.height//2 - 2 , 10,5)
                    yellow_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()

                elif event.key == pygame.K_RCTRL and len(red_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(red.x , red.y + red.height//2 - 2 , 10,5)
                    red_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()

            if event.type == RED_HIT:
                red_health -= 1
                BULLET_HIT_SOUND.play()

            if event.type == YELLOW_HIT:
                yellow_health -= 1
                BULLET_HIT_SOUND.play()
            
        winner_text = ""
        if red_health <= 0:
            winner_text = "Yellow wins!"

        if yellow_health <= 0:
            winner_text = "Red wins!"

        if winner_text != "":
            draw_winner(winner_text)
            break
        
        key_pressed = pygame.key.get_pressed()
        yellow_movement(key_pressed , yellow)
        red_movement(key_pressed , red)
        handle_bullet(yellow_bullets , red_bullets , yellow , red)
        draw_window(red , yellow , red_bullets , yellow_bullets , red_health , yellow_health)

main()

if __name__ == "__main__":
    main()




