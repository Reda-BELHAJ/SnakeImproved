import pygame

sprite_cell = pygame.image.load("Cell.png")

def draw_grass(Surface):
        for row in range(30):
            for col in range(30):
                grass_rect = pygame.Rect(col * 16, row * 16, 16, 16)
                Surface.blit(sprite_cell, grass_rect)

finsurf = pygame.Surface((480, 480), pygame.SRCALPHA)
draw_grass(finsurf)
pygame.image.save(finsurf, "BG.png")