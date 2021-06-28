import pygame
import random
from pygame.math import Vector2

cell_size = 16
cell_number = 38

class Particle:
    def __init__(self, x, y) -> None:
        self.position = Vector2(x * cell_size, y * cell_size)
        self.radius = random.randint(1, 6)
    
    def animate(self, Surface):
        self.position.x += random.randint(0, 20)/10 - 1
        self.position.y += -2
        self.radius -= 0.05
        pygame.draw.circle(Surface, (255, 255, 255), (self.position.x, self.position.y), self.radius)