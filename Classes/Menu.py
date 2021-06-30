import pygame

class Menu:
    def __init__(self, font, text, color) -> None:
        self.text_obj = font.render(text, 1, color)
        self.text_rect = self.text_obj.get_rect()

        self.button = pygame.Rect(50, 100, 200, 50)
    
    def draw_text(self, x, y, Surface):
        self.text_rect.topleft = (x, y)
        Surface.blit(self.text_obj, self.text_rect)