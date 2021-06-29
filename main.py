import pygame
from pygame.math import Vector2
from Classes.GAME import GAME
from Classes.Particle import Particle
from Classes.Menu import Menu

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

SCREEN_UPDATE = pygame.USEREVENT

RED = (128, 0, 0)
WHITE = (255, 255, 255)
DARK_GREEN = (63, 70, 39)
LIGHT_GREEN = (213, 212, 184)
BLACK = (0, 0, 0)


def animate(timer, particles_anim, index):
    particles_anim.append(Particle(game.anim_pos[index].x, game.anim_pos[index].y, colors[index]))
    timer += 1
    if timer < 30:
        for particle in particles_anim:
            particle.draw(display)
            if particle.radius <= 0:
                particles_anim.remove(particle)
    else:
        timer = 0
        game.anim_pos[index] = Vector2(-1,-1)
        particles_anim = []
    
    return timer, particles_anim

if __name__ == '__main__':
    
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
    display = pygame.Surface((608, 608))

    clock  = pygame.time.Clock()
    pygame.display.set_caption('Snake Game')

    font = pygame.font.SysFont(None, 30)

    pygame.time.set_timer(SCREEN_UPDATE, 150)

    menu = Menu(font, "main menu", WHITE)
    game = GAME(1)

    particles_anim =  []
    colors = [DARK_GREEN, pygame.Color('Red'), pygame.Color('Gold')]

    timer = 0

    running = True

    while running:
        screen.fill(BLACK)

        menu.draw_text(40, 40, screen)

        pygame.display.update()
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    running = False
                    break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                        running = False
                        break
                if event.key == pygame.K_RETURN:
                    game.playing = True
                    running = False
                    break

    while game.playing:
        clock.tick(60)
        screen.fill(BLACK)
        display.fill(LIGHT_GREEN)

        if game.game_over:
            break

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                game.playing = False
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    game.playing = False
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
                    
            if event.type == SCREEN_UPDATE:
                game.update()

        game.draw_elements(display)

        for i, anim in enumerate(game.anim_pos):
            if anim != Vector2(-1,-1) :
                timer, particles_anim = animate(timer, particles_anim, i)

        # le trou: Feature
        # UI

        screen.blit(display, (100, 100))
        
        pygame.display.update()
        pygame.display.flip()

    pygame.quit()