import pygame
import random
from pygame.math import Vector2

cell_size = 16
cell_number = 30

class Rocket:
    def __init__(self, mode) -> None:
        self.mode = mode
        self.sprite = self.sprite()
        self.randomize()
        self.acc = 0.05

    def sprite(self):
        if self.mode == 0:
            return pygame.image.load("Assets/Spear.png")
        elif self.mode == 1:
            return pygame.image.load("Assets/Spear.png")

    def randomize(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = 0
        self.position = Vector2(self.x, self.y)
    
    def move(self):
        self.y += 1 * self.acc
        self.position = Vector2(self.x, self.y)
    
    def draw_rocket(self, Surface):
        if self.position.y * cell_size <= 800:
            self.move()
            self.rocket_rect = pygame.Rect(int(self.position.x * cell_size), int(self.position.y * cell_size), cell_size, cell_size * 3)
            self.small_rect = pygame.Rect(int(self.position.x * cell_size), int(self.position.y * cell_size) + cell_size + cell_size, cell_size, cell_size)

            if self.mode == 0:
                for i in range(3):
                    rect = pygame.Rect(int(self.position.x * cell_size), int(self.position.y * cell_size) + i * cell_size, cell_size, cell_size)
                    Surface.blit(self.sprite, rect)
                
            elif self.mode == 1:
                pygame.draw.rect(Surface, pygame.Color('Black'), self.rocket_rect)