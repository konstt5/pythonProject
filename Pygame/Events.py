import pygame

pygame.init()

size = width, height = 800, 600
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
fps = 60

screen.fill(pygame.Color('black'))

running = True
while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pygame.draw.circle(screen, (255, 255, 255), event.pos, 20)
        if event.type == pygame.MOUSEMOTION and event.buttons[0] == 1:
            pygame.draw.circle(screen, (255, 255, 255), event.pos, 10)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            screen.fill(pygame.Color('black'))

    pygame.display.set_caption("%d" % clock.get_fps())

    pygame.display.flip()
    clock.tick(fps)

pygame.quit()