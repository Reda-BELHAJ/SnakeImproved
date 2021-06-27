from Classes.Bomb import Bomb
import pygame
from .Coin import Coin
from .Snake import Snake
from .Bomb import Bomb
from .Rocket import Rocket

cell_size = 16
cell_number = 50

class GAME():
    def __init__(self) -> None:
        self.coin = Coin()
        self.snake = Snake()
        self.bombs = [Bomb()]
        self.rockets = []

        self.condition = 8
        self.crowd = 2
        self.count = 0

    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()

        if self.count >= self.condition:
            self.bombs.insert(0, Bomb())
            self.condition += 8
        if self.count >= self.crowd:
            self.rockets.insert(0, Rocket())
            self.condition += 2

    def draw_elements(self, screen):
        self.coin.draw_coin(screen)
        self.snake.draw_snake(screen)

        for bomb in self.bombs:
            bomb.draw_bomb(screen)
        
        for rocket in self.rockets:
            rocket.draw_rocket(screen)

    def check_collision(self):
        if self.coin.position == self.snake.body[0]:
            self.count += 1
            self.coin.randomize()
            self.snake.add_block()

        for bomb in self.bombs:
            if bomb.position == self.snake.body[0]:
                self.game_over()

    def check_fail(self):
        if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
            self.game_over()
        
        for block in self.snake.body[1:] :
            if block == self.snake.body[0]:
                self.game_over()

    def game_over(self):
        pygame.quit()