import pygame
import random
from pygame.math import Vector2

cell_size = 16
cell_number = 30

class Particle:
    def __init__(self, x, y, color) -> None:
        self.position = Vector2(x * cell_size, y * cell_size)
        self.position_vel = Vector2(random.randrange(0, 30) /10 - 1, random.randrange(0, 30) /10 - 1)
        self.radius = random.randint(1, 4)
        self.color = color
        self.lifetime = 0

    def draw(self, Surface):
        self.lifetime += 1 
        if self.lifetime < 20:
            self.position.x += self.position_vel.x
            self.position.y += self.position_vel.y
            self.radius -= 0.1
            pygame.draw.circle(Surface, self.color, self.position, self.radius)