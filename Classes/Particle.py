import pygame
import random
from pygame.math import Vector2

class Particle:
    def __init__(self, x, y) -> None:
        self.position = Vector2(x, y)
        self.radius = random.randint(4, 6)
    
    def animate(self):
        self.position.x += random.randint(0, 20) / 10
        self.position.y += -2