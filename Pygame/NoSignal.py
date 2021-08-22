import pygame
import random

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

fps = 40

def draw():
    screen.fill(pygame.Color('black'))
    for i in range(10000):
        screen.fill(pygame.Color('white'), (800 * random.random(), 600 * random.random(), 1, 1))

running = True
while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False

    pygame.display.set_caption("%d" % clock.get_fps())
    draw()

    pygame.display.flip()
    clock.tick(fps)

pygame.quit()