import pygame
import random
from pygame.math import Vector2

image = "blue_gem.png"

cell_size = 16
cell_number = 25

class Coin:
    def __init__(self) -> None:
        # self.sprite = pygame.image.load("Assets/" + image).convert_alpha()
        self.randomize()

    def randomize(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.position = Vector2(self.x, self.y)
    
    def draw_coin(self, Surface):
        coin_rect = pygame.Rect(int(self.position.x * cell_size), int(self.position.y * cell_size), cell_size, cell_size)
        pygame.draw.rect(Surface, pygame.Color('Gold'), coin_rect)
        # Surface.blit(self.sprite, coin_rect)