import pygame
import random
from pygame.math import Vector2

cell_size = 16
cell_number = 25

class Rocket:
    def __init__(self) -> None:
        self.randomize()
        self.acc = 0.1

    def randomize(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = 0
        self.position = Vector2(self.x, self.y)
    
    def move(self):
        self.y += 1 * self.acc
        self.position = Vector2(self.x, self.y)
    
    def draw_rocket(self, Surface):
        self.move()
        rocket_rect = pygame.Rect(int(self.position.x * cell_size), int(self.position.y * cell_size), cell_size, cell_size * 3)
        pygame.draw.rect(Surface, pygame.Color('Blue'), rocket_rect)