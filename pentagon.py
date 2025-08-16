import pygame
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pentagon_image = pygame.image.load("pentagon.png")
blit_positions = []

running = True
while running:
    screen.fill((255, 255, 255))  

    for pos in blit_positions:
        rect = pentagon_image.get_rect(center=pos)
        screen.blit(pentagon_image, rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  
                blit_positions.append(event.pos)

    pygame.display.flip()
pygame.quit()
