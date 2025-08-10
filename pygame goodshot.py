import pygame
import random
pygame.init()
WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Good Shot")
font = pygame.font.SysFont(None, 50)
clock = pygame.time.Clock()

bg = pygame.image.load("space.png")
alien_img = pygame.image.load("alien.png")
alien_rect = alien_img.get_rect(center=(WIDTH // 2, HEIGHT // 2))
message = ""

def place_alien():
    alien_rect.centerx = random.randint(50, WIDTH - 50)
    alien_rect.centery = random.randint(50, HEIGHT - 50)

place_alien()

run = True
while run:
    screen.blit(bg, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if alien_rect.collidepoint(event.pos):
                message = "Good Shot"
            else:
                message = "You missed"
            place_alien()

    screen.blit(alien_img, alien_rect)
    text = font.render(message, True, (255, 255, 255))
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, 30))

    pygame.display.flip()
    clock.tick(60)
pygame.quit()

