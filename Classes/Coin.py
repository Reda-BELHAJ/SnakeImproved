import pygame
import random
from pygame.math import Vector2
from pygame.sprite import Sprite

cell_size = 16
cell_number = 38

coins = []

for i in range(5):
    coins.append(pygame.image.load("Assets/Coin/Coin"+ str(int(i + 1)) +".png"))

class Coin(Sprite):
    def __init__(self, mode) -> None:
        self.mode = mode
        self.sprite = self.sprite()
        super().__init__()
        self.current_sprite = -1 
        self.randomize()

    def sprite(self):
        if self.mode == 0:
            return pygame.image.load("Assets/Coin.png")
        elif self.mode == 1:
            return coins[0]

    def randomize(self):
        self.x = random.randint(1, cell_number - 2)
        self.y = random.randint(1, cell_number - 2)
        self.position = Vector2(self.x, self.y)
    
    def draw_coin(self, Surface):
        self.current_sprite += 0.2 

        if self.current_sprite >= len(coins):
            self.current_sprite = -1 

        self.coin_rect = pygame.Rect(int(self.position.x * cell_size), int(self.position.y * cell_size), cell_size, cell_size)

        if self.mode == 1:   
            self.sprite = coins[int(self.current_sprite)]
        
        Surface.blit(self.sprite, self.coin_rect)