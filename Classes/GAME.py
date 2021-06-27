import pygame
from .Coin import Coin
from .Snake import Snake

cell_size = 40
cell_number = 20

class GAME():
    def __init__(self) -> None:
        self.coin = Coin()
        self.snake = Snake()
        self.count = 0

    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()

    def draw_elements(self, screen):
        self.coin.draw_coin(screen)
        self.snake.draw_snake(screen)

    def check_collision(self):
        if self.coin.position == self.snake.body[0]:
            self.count += 1
            self.coin.randomize()
            self.snake.add_block()

    def check_fail(self):
        if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
            self.game_over()
        
        for block in self.snake.body[1:] :
            if block == self.snake.body[0]:
                self.game_over()

    def game_over(self):
        pygame.quit()