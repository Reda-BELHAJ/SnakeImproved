import pygame
from pygame.locals import *
from pygame.math import Vector2
from Classes.GAME import GAME
from Classes.Particle import Particle
from Classes.Menu import Menu

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

SCREEN_UPDATE = pygame.USEREVENT

WHITE = (255, 255, 255)
DARK_GREEN = (63, 70, 39)
LIGHT_GREEN = (213, 212, 184)
BLACK = (0, 0, 0)
RED = (207, 104, 84)
GOLD = (255, 159, 0)

def menu_screen(running, playing):
    while running:
        screen.fill(BLACK)

        menu.draw_text(40, 40, screen)

        pygame.display.update()
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    running = 0
                    break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = 0
                    playing = 1
                    break
                if event.key == pygame.K_RETURN:
                    playing = 1
                    running = 0
                    break
    
    return running, playing

def game_loop(timer, particles_anim, running, playing, mode, fake_display, display):
    while playing:
        clock.tick(60)
        screen.fill(BLACK)
        fake_display.fill(LIGHT_GREEN)

        if game.game_over:
            running, playing = game.refresh(mode)
            break

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = 0
                playing = 0
                break
            if event.type == VIDEORESIZE:
                display = pygame.display.set_mode(event.size, HWSURFACE|DOUBLEBUF|RESIZABLE)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = 1
                    playing = 0
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

        game.draw_elements(fake_display)

        for i, anim in enumerate(game.anim_pos):
            if anim != Vector2(-1,-1) :
                timer, particles_anim = animate(timer, particles_anim, i)
        
        display.blit(pygame.transform.scale(fake_display, display.get_rect().size), (0, 0))
        screen.blit(display, (50, 50))
        pygame.display.flip()
    
    return running, playing

def animate(timer, particles_anim, index):
    particles_anim.append(Particle(game.anim_pos[index].x, game.anim_pos[index].y, colors[index]))
    timer += 1
    if timer < 30:
        for particle in particles_anim:
            particle.draw(fake_display)
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
    display = pygame.Surface((700, 700),HWSURFACE|DOUBLEBUF|RESIZABLE)
    fake_display = pygame.Surface((480, 480))

    clock  = pygame.time.Clock()
    pygame.display.set_caption('Snake Game')

    font = pygame.font.SysFont(None, 30)

    pygame.time.set_timer(SCREEN_UPDATE, 150)
    countdown = 5

    menu = Menu(font, "main menu", WHITE)
    game = GAME(1)

    particles_anim =  []
    if game.mode == 1:
        colors = [DARK_GREEN, RED, GOLD]
    else:
        colors = [DARK_GREEN] * 3

    timer = 0
    running = 1

    while running:
        if not game.playing:
            running, game.playing = menu_screen(running, game.playing)
            
        running, game.playing = game_loop(timer, particles_anim, running, game.playing, game.mode, fake_display, display)

    pygame.quit()
