import pygame
import random
from pygame.math import Vector2


cell_size = 16
cell_number = 38

class Coin:
    def __init__(self) -> None:
        self.sprite = pygame.image.load("Assets/Coin.png")
        self.randomize()

    def randomize(self):
        self.x = random.randint(1, cell_number - 2)
        self.y = random.randint(1, cell_number - 2)
        self.position = Vector2(self.x, self.y)
    
    def draw_coin(self, Surface):
        self.coin_rect = pygame.Rect(int(self.position.x * cell_size), int(self.position.y * cell_size), cell_size, cell_size)
        # pygame.draw.rect(Surface, pygame.Color('Gold'), self.coin_rect)
        Surface.blit(self.sprite, self.coin_rect)