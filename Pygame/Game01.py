import pygame

if __name__ == "__main__":
    pygame.init()

    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("The Game")
    # img = pygame.image.load("C:\_Local\Жерников\Downloads\1.gif")
    # pygame.display.set_icon(img)
    font = pygame.font.SysFont("arial", 26)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    fr = font.render("Первая игра", 1, RED, GREEN)

    # основной цикл, обработка событий
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
        screen.blit(fr, (100, 100))
        pygame.display.update()