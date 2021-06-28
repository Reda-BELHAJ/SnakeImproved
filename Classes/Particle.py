import pygame
import random
from pygame.math import Vector2

cell_size = 16
cell_number = 38

WHITE = (255, 255, 255)

class Particle:
    def __init__(self, x, y) -> None:
        self.position = Vector2(x * cell_size, y * cell_size)
        self.position_vel = Vector2(random.randrange(-3, 3) * 5, random.randrange(-10, -1) * 5)
        self.radius = random.randint(4, 6)
        self.lifetime = 0

    def draw(self, Surface):
        self.lifetime += 1 
        if self.lifetime < 20:
            self.position.x += self.position_vel.x
            self.position.y += self.position_vel.y
            self.radius -= 0.1
            pygame.draw.circle(Surface, WHITE, self.position, self.radius)