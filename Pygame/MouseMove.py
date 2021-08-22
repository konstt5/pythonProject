import pygame

pygame.init()

size = width, height = 800, 600
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
fps = 60

screen.fill(pygame.Color('black'))

x, y = 400, 300
r = 40
dx, dy = 0, 0
flag = False
running = True
while running:
    screen.fill(pygame.Color('black'))
    pygame.draw.circle(screen, (255, 255, 255), (x, y), r)

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if (event.pos[0] - x) ** 2 + (event.pos[1] - y) ** 2 <= (r * r):
                flag = True
                dx = event.pos[0] - x
                dy = event.pos[1] - y
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            flag = False
        if event.type == pygame.MOUSEMOTION and flag:
            x, y = (event.pos[0] - dx), (event.pos[1] - dy)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            x, y = 400, 300
            flag = False
            screen.fill(pygame.Color('black'))
            pygame.draw.circle(screen, (255, 255, 255), (400, 300), r)

    pygame.display.set_caption("%d" % clock.get_fps())

    pygame.display.flip()
    clock.tick(fps)

pygame.quit()