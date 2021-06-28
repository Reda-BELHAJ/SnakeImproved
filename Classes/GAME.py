import pygame
from .Coin import Coin
from .Snake import Snake, Block
from .Bomb import Bomb
from .Rocket import Rocket
from .Particle import Particle

cell_size = 16
cell_number = 38

particles_anim =  lambda block :[Particle(block.x, block.y)] * 20

class GAME():
    def __init__(self) -> None:
        self.coin = Coin()
        self.snake = Snake()
        self.bombs = [Bomb()]
        self.rockets = []
        self.particles = []

        self.condition = 1
        self.crowd = 0
        self.count = 0

        self.game_timer = 0

        # self.acc = 0.1
        # self.difficulty = 0

    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()
    
    def check_timer(self):
        if self.count >= self.crowd:
            self.game_timer += 1
            if self.game_timer > 50:
                self.game_timer = 0
                self.rockets.append(Rocket())


    def draw_elements(self, screen):
        # self.draw_grass(screen)
        self.coin.draw_coin(screen)
        self.snake.draw_snake(screen)
        self.check_timer()

        if self.count >= self.condition:
            self.bombs.insert(0, Bomb())
            self.condition += 1

        for bomb in self.bombs:
            bomb.draw_bomb(screen)
        
        for rocket in self.rockets:
            rocket.draw_rocket(screen)

        for particle in self.particles:
            particle.draw(screen)

    def check_position(self):
        for bomb in self.bombs:
            if self.coin.position != bomb.position:
                self.coin.randomize()
            else:
                self.check_position()

    def check_collision(self):
        if self.coin.position == self.snake.body[0]:
            self.count += 1
            self.check_position()
            self.snake.add_block()

        for rocket in self.rockets:
            for i, block in enumerate(self.snake.body[:-1]):
                if rocket.rocket_rect.colliderect(Block(block.x, block.y).rect):
                    self.snake.remove_block(i)
                    self.particles = particles_anim(block)

    def check_fail(self):
        if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
            self.game_over()
        
        for block in self.snake.body[1:] :
            if block == self.snake.body[0]:
                self.game_over()

        for rocket in self.rockets:
            if rocket.rocket_rect.colliderect(Block(self.snake.body[0].x, self.snake.body[0].y).rect):
                self.game_over()

        for bomb in self.bombs:
            if bomb.position == self.snake.body[0]:
                self.game_over()
                    
    # def draw_grass(self, Surface):
    #     DARKER_GREEN = (19, 61, 30)
    #     for row in range(cell_number):
    #         if row % 2 == 0:
    #             for col in range(cell_number):
    #                 if col % 2 == 0:
    #                     grass_rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
    #                     pygame.draw.rect(Surface, DARKER_GREEN, grass_rect)
    #         else:
    #             for col in range(cell_number):
    #                 if col % 2 == 1:
    #                     grass_rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
    #                     pygame.draw.rect(Surface, DARKER_GREEN, grass_rect)

    def game_over(self):
        pygame.quit()