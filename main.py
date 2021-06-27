import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

GREY = (64, 64, 64)
RED = (128, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
DARK_YELLOW = (128, 128, 0)
BLACK = (0, 0, 0)

if __name__ == '__main__':
    
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
    clock  = pygame.time.Clock()
    pygame.display.set_caption('Snake Game')

    getTicksLastFrame = 0

    running = True

    while running:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    break
            if event.type == pygame.QUIT:
                running = False
                break
        
        pygame.display.flip()

    pygame.quit()