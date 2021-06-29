import pygame
import random
from pygame.math import Vector2

cell_size = 16
cell_number = 38

class Block:
    def __init__(self, x, y) -> None:
        self.sprite = pygame.image.load("Assets/Block.png")
        self.rect = pygame.Rect(int(x * cell_size), int(y * cell_size), cell_size, cell_size)

class Snake:
    def __init__(self) -> None:
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(1, 0)

        self.new_block = False
        self.index = -1
    
    def draw_snake(self, Surface):
        for block in self.body:
            b = Block(block.x, block.y)
            block_rect = b.rect
            # pygame.draw.rect(Surface, pygame.Color('Green'), block_rect)
            Surface.blit(b.sprite, block_rect)
            

    def move_snake(self):
        if self.new_block:
            body_copy = self.body[:]
            self.new_block = False
        else:
            body_copy = self.body[:-1]

        if self.index != -1:
            body_copy = self.body[:self.index]
            self.index = -1

        body_copy.insert(0, body_copy[0] + self.direction)
        self.body = body_copy[:]

    def add_block(self):
        self.new_block = True

    def remove_block(self, index):
        self.index = index
