import pygame

pygame.init()

x = 800
y = 600

screen = pygame.display.set_mode((x,y))
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0,0,0))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
