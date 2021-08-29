import pygame
import random

pygame.init()

size = width, height = 800, 600
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
fps = 60

def loadImage(name):
    fullname = "Data/" + name
    try:
        if name[-2:] == "jpg":
            image = pygame.image.load(fullname).convert()
        else:
            image = pygame.image.load(fullname).convert_alpha()
    except:
        print("Cannot load image: ", name)
        raise SystemExit()

    return image

image = loadImage("brick.png")
w, h = image.get_width(), image.get_height()
x, y = 10, 10
mx, my = None,None

allSprites = pygame.sprite.Group()

for i in range(12):
    x = 10
    for j in range(18):
        brick = pygame.sprite.Sprite()
        brick.image = image
        brick.rect = image.get_rect()
        allSprites.add(brick)

        brick.rect.x = x
        brick.rect.y = y
        x = x + w
    y = y + h

def updateSprite(sprite):
    if mx == None or my == None:
        pass
    else:
        dx = 10 * (mx - sprite.rect.x) / width
        dy = 10 * (my - sprite.rect.y) / height

        sprite.rect = sprite.rect.move(int(dx) + random.randint(-1, 1), int(dy) + random.randint(-1, 1))

running = True
while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEMOTION:
            mx, my = event.pos[0], event.pos[1]

    pygame.display.set_caption("%d" % clock.get_fps())

    screen.fill((0, 0, 0))
    for sprite in allSprites:
        updateSprite(sprite)
    allSprites.draw(screen)

    pygame.display.flip()
    clock.tick(fps)

pygame.quit()