import pygame
import random
from pygame.math import Vector2

image = "bomb.png"

cell_size = 16
cell_number = 38

bombs = []

for i in range(4):
    bombs.append(pygame.image.load("Assets/Bomb/Bomb"+ str(int(i + 1)) +".png"))

class Bomb:
    def __init__(self, mode) -> None:
        self.mode = mode
        self.sprite = self.sprite()
        self.current_sprite = -1 
        self.randomize()

    def sprite(self):
        if self.mode == 0:
            return pygame.image.load("Assets/" + image).convert_alpha()
        elif self.mode == 1:
            return bombs[0]
    
    def randomize(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.position = Vector2(self.x, self.y)
    
    def draw_bomb(self, Surface):
        self.current_sprite += 0.2 

        if self.current_sprite >= len(bombs):
            self.current_sprite = -1 
            
        self.bomb_rect = pygame.Rect(int(self.position.x * cell_size), int(self.position.y * cell_size), cell_size, cell_size)

        self.sprite = bombs[int(self.current_sprite)]

        if self.mode == 0:
            Surface.blit(self.sprite, self.bomb_rect)
        elif self.mode == 1:
            Surface.blit(self.sprite, self.bomb_rect)
            # Change the image asset Animated Bomb