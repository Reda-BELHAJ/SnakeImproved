import pygame
from Classes.Coin import Coin
from Classes.Snake import Snake

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

SCREEN_UPDATE = pygame.USEREVENT

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

    pygame.time.set_timer(SCREEN_UPDATE, 150)

    coin = Coin()
    snake = Snake()

    running = True

    while running:
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    break
            if event.type == pygame.QUIT:
                running = False
                break
            if event.type == SCREEN_UPDATE:
                snake.move_snake()
        
        coin.draw_coin(screen)
        snake.draw_snake(screen)
        
        pygame.display.update()
        pygame.display.flip()

        clock.tick(60)

    pygame.quit()