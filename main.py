import pygame
from pygame.math import Vector2
from Classes.GAME import GAME

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

    game = GAME()

    running = True

    while running:
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    break
                if event.key == pygame.K_UP:
                    if game.snake.direction.y != 1:
                        game.snake.direction = Vector2(0, -1)
                if event.key == pygame.K_DOWN:
                    if game.snake.direction.y != -1:
                        game.snake.direction = Vector2(0, 1)
                if event.key == pygame.K_LEFT:
                    if game.snake.direction.x != 1:
                        game.snake.direction = Vector2(-1, 0)
                if event.key == pygame.K_RIGHT:
                    if game.snake.direction.x != -1:
                        game.snake.direction = Vector2(1, 0)
                    
            if event.type == pygame.QUIT:
                running = False
                break
            if event.type == SCREEN_UPDATE:
                game.update()
        
        game.draw_elements(screen)
        
        pygame.display.update()
        pygame.display.flip()

        clock.tick(60)

    pygame.quit()