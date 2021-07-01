import pygame
from .Coin import Coin
from .Snake import Snake, Block
from .Bomb import Bomb
from .Rocket import Rocket
from pygame.math import Vector2

cell_size = 16
cell_number = 30

sprite_cell = pygame.image.load("Assets/Cell.png")
bg = pygame.image.load("Assets/BG.png")
bg2 = pygame.image.load("Assets/BG2.png")

class GAME():
    def __init__(self, mode) -> None:
        self.playing = 0

        self.mode = mode
        # Classic mode 
        # Colorfull mode with assets etc

        self.coin = Coin(self.mode)

        self.moving_coin = pygame.sprite.Group()
        self.moving_coin.add(self.coin)

        self.snake = Snake(self.mode)
        self.bombs = [Bomb(self.mode)]
        self.rockets = []

        self.condition = 4
        self.crowd = 2
        self.count = 0

        self.anim_pos = [Vector2(-1,-1), Vector2(-1,-1), Vector2(-1,-1)]

        self.game_timer = 0

        self.game_over = False

        # self.acc = 0.1
        # self.difficulty = 0

    def refresh(self, mode):
        self.__init__(mode)
        return 1, 0

    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()
        self.rem_rockets()
    
    def rem_rockets(self):
        for rocket in self.rockets:
            if not rocket.out_of_frame():
                self.rockets.remove(rocket)
    
    def check_timer(self):
        if self.count >= self.crowd:
            self.game_timer += 1
            if self.game_timer > 50:
                self.game_timer = 0
                self.rockets.append(Rocket(self.mode))

    def draw_elements(self, screen):
        if self.mode == 0:
            screen.blit(bg, (0, 0))
        elif self.mode == 1:
            screen.fill((155, 199, 167))
        self.coin.draw_coin(screen)
        self.snake.draw_snake(screen)
        self.check_timer()

        if self.count >= self.condition:
            self.bombs.insert(0, Bomb(self.mode))
            self.condition = self.condition * 2

        for rocket in self.rockets:
            rocket.draw_rocket(screen)

        for bomb in self.bombs:
            bomb.draw_bomb(screen)

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
                    self.anim_pos[0] = Vector2(block.x, block.y)
            
            for bomb in self.bombs:
                if bomb.bomb_rect.colliderect(rocket.small_rect):
                    self.anim_pos[1] = bomb.position
                    if len(self.bombs) > 1 :
                        self.bombs.remove(bomb)
                    else:
                        bomb.randomize()
            if rocket.rocket_rect.colliderect(self.coin.coin_rect):
                self.anim_pos[2] = Vector2(self.coin.x, self.coin.y)
                self.coin.randomize()


    def check_fail(self):
        if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
            self.game_over = True
        
        for block in self.snake.body[1:] :
            if block == self.snake.body[0]:
                self.game_over = True

        for rocket in self.rockets:
            if rocket.rocket_rect.colliderect(Block(self.snake.body[0].x, self.snake.body[0].y).rect):
                self.game_over = True

        for bomb in self.bombs:
            if bomb.position == self.snake.body[0]:
                self.game_over = True