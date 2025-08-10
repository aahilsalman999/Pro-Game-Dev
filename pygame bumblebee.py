import pygame
import random
pygame.init()
WIDTH, HEIGHT = 600, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bee Flower Game")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 40)
bg = pygame.image.load("space.png")
bee_img = pygame.image.load("bee.png")
flower_img = pygame.image.load("flower.png")
bee = bee_img.get_rect(center=(100, 100))
flower = flower_img.get_rect(center=(200, 200))

score = 0
game_over = False
start_ticks = pygame.time.get_ticks()
time_limit = 60  

def place_flower():
    flower.centerx = random.randint(70, WIDTH - 70)
    flower.centery = random.randint(70, HEIGHT - 70)

place_flower()

def draw_text(text, pos, color=(255, 255, 255)):
    label = font.render(text, True, color)
    screen.blit(label, pos)

run = True
while run:
    dt = clock.tick(60)  
    screen.blit(bg, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    if not game_over:
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:  bee.x -= 2
        if keys[pygame.K_RIGHT]: bee.x += 2
        if keys[pygame.K_UP]:    bee.y -= 2
        if keys[pygame.K_DOWN]:  bee.y += 2

        if bee.colliderect(flower):
            score += 10
            place_flower()

        seconds_passed = (pygame.time.get_ticks() - start_ticks) / 1000
        time_left = max(0, time_limit - int(seconds_passed))
        if time_left == 0:
            game_over = True

        screen.blit(flower_img, flower)
        screen.blit(bee_img, bee)
        draw_text(f"Score: {score}", (10, 10))
        draw_text(f"Time: {time_left}", (WIDTH - 140, 10))
    else:
        screen.fill((255, 192, 203))  
        draw_text(f"Time's Up! Final Score: {score}", (WIDTH // 2 - 200, HEIGHT // 2 - 20), (200, 0, 0))

    pygame.display.flip()
