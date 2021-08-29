import pygame
import random
from threading import Timer

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

bananaSprites = pygame.sprite.Group()
borderSprites = pygame.sprite.Group()

class Banana(pygame.sprite.Sprite):
    image = loadImage("banana_full.png")
    image_open = loadImage("banana_ready.png")

    w, h = image.get_width(), image.get_height()

    def __init__(self):
        super().__init__(bananaSprites)
        self.image = Banana.image
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(Banana.w, width - Banana.w)
        self.rect.y = random.randint(Banana.h, 2 * Banana.h)
        self.vy = random.randint(1, 6)

    def mouseclick(self, pos):
        if self.rect.collidepoint(pos):
            self.image = Banana.image_open
            x, y = self.rect.x, self.rect.y
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y

    def update(self):
        self.rect.y = self.rect.y + self.vy
        if pygame.sprite.spritecollideany(self, borderSprites):
            self.vy = 0

class Border(pygame.sprite.Sprite):
    def __init__(self, x1, y1, x2, y2):
        super().__init__(borderSprites)
        self.image = pygame.Surface((x2 - x1, y2 - y1))
        self.image.fill((255, 255, 0))
        self.rect = pygame.Rect(x1, y1, x2, y2, )

def addBanana():
    Banana()
    timer = Timer(1, addBanana)
    timer.start()

Border(5, 5, width - 5, 6)
Border(5, height - 6, width - 5, height - 5)
Border(5, 5, 6, height - 5)
Border(width - 6, 5, width - 5, height - 5)

addBanana()

running = True
while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            for banana in bananaSprites:
                banana.mouseclick(event.pos)

    pygame.display.set_caption("%d" % clock.get_fps())

    screen.fill((0, 0, 0))
    for sprite in bananaSprites:
        sprite.update()
    bananaSprites.draw(screen)
    borderSprites.draw(screen)

    pygame.display.flip()
    clock.tick(fps)

pygame.quit()