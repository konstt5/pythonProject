import pygame
import random
from threading import Timer

pygame.init()

size = width, height = 800, 600
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
fps = 60
bananaCount = 0
bananaCatch = 0

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
textSprites = pygame.sprite.Group()

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
        self.catched = False

    def mouseclick(self, pos):
        if self.vy > 0 and self.rect.collidepoint(pos):
            self.image = Banana.image_open
            x, y = self.rect.x, self.rect.y
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y

            if not self.catched:
                global bananaCatch
                bananaCatch = bananaCatch + 1
                self.catched = True

    def update(self):
        self.rect.y = self.rect.y + self.vy
        if self.vy > 0 and pygame.sprite.spritecollideany(self, borderSprites):
            self.vy = 0

class Text(pygame.sprite.Sprite):
    def __init__(self, text, x, y):
        super().__init__(textSprites)
        self.text = text
        self.font = pygame.font.Font(None, 30)
        self.image = self.font.render(self.text, 1, (255, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.image = self.font.render(self.text, 1, (255, 255, 0))

class Border(pygame.sprite.Sprite):
    def __init__(self, x1, y1, x2, y2):
        super().__init__(borderSprites)
        self.image = pygame.Surface((x2 - x1, y2 - y1))
        self.image.fill((255, 255, 0))
        self.rect = pygame.Rect(x1, y1, x2, y2, )

class perpetualTimer():

    def __init__(self, t, hFunction):
        self.t = t
        self.hFunction = hFunction
        self.thread = Timer(self.t, self.handle_function)

    def handle_function(self):
        self.hFunction()
        self.thread = Timer(self.t, self.handle_function)
        self.thread.start()

    def start(self):
        self.thread.start()

    def cancel(self):
        self.thread.cancel()

def addBanana():
    Banana()
    global bananaCount
    bananaCount = bananaCount + 1

Border(5, 5, width - 5, 6)
Border(5, height - 6, width - 5, height - 5)
Border(5, 5, 6, height - 5)
Border(width - 6, 5, width - 5, height - 5)

countText = Text("Bananas: 0", 10, 10)
catchText = Text("Catched: 0", 200, 10)

timer = perpetualTimer(1, addBanana)
timer.start()

running = True
while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            for banana in bananaSprites:
                banana.mouseclick(event.pos)

    pygame.display.set_caption("Catch banana (fps %d)" % clock.get_fps())

    screen.fill((0, 0, 0))

    for sprite in bananaSprites:
        sprite.update()
    for sprite in textSprites:
        sprite.update()

    countText.__setattr__("text", f"Bananas: {bananaCount}")
    catchText.__setattr__("text", f"Catched: {bananaCatch}")

    bananaSprites.draw(screen)
    borderSprites.draw(screen)
    textSprites.draw(screen)

    pygame.display.flip()
    clock.tick(fps)

timer.cancel()
pygame.quit()