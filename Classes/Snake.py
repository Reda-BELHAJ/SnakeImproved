import pygame
import random
from pygame.math import Vector2

cell_size = 40
cell_number = 20

class Snake:
    def __init__(self) -> None:
        self.body = [Vector2(5, 10), Vector2(6, 10), Vector2(7, 10)]
        self.direction = Vector2(1, 0)
    
    def draw_snake(self, Surface):
        for block in self.body:
            block_rect = pygame.Rect(int(block.x * cell_size), int(block.y * cell_size), cell_size, cell_size)
            pygame.draw.rect(Surface, pygame.Color('Blue'), block_rect)

    def move_snake(self):
        body_copy = self.body[:-1]
        body_copy.insert(0, body_copy[0] + self.direction)
        self.body = body_copy[:]