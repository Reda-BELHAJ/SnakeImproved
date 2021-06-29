import pygame
import random
from pygame.math import Vector2

image = "bomb.png"

cell_size = 16
cell_number = 38

class Bomb:
    def __init__(self, mode) -> None:
        self.mode = mode
        self.sprite = pygame.image.load("Assets/" + image).convert_alpha()
        self.randomize()

    def randomize(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.position = Vector2(self.x, self.y)
    
    def draw_bomb(self, Surface):
        self.bomb_rect = pygame.Rect(int(self.position.x * cell_size), int(self.position.y * cell_size), cell_size, cell_size)
        if self.mode == 0:
            pygame.draw.rect(Surface, pygame.Color('Red'), self.bomb_rect)
        elif self.mode == 1:
            Surface.blit(self.sprite, self.bomb_rect)
            # Change the image asset