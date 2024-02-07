import pygame
from ..settings import WIDTH, HEIGHT, BG_COLOR, BORDER_COLOR, BORDER_WIDTH, BORDER_HEIGHT

class Page:
    def __init__(self, title, border = True) -> None:
        self.title = title
        self.border = border
    
    def bg_render(self, screen, color = BG_COLOR):
        screen.fill(color)

    def border_render(self, screen, color = BORDER_COLOR):
        pygame.draw.rect(screen, color, (0, 0, WIDTH, BORDER_HEIGHT))
        pygame.draw.rect(screen, color, (0, HEIGHT-BORDER_WIDTH, WIDTH, BORDER_WIDTH))
        pygame.draw.rect(screen, color, (0, 0, BORDER_HEIGHT, HEIGHT))
        pygame.draw.rect(screen, color, (WIDTH-BORDER_HEIGHT, 0, BORDER_HEIGHT, HEIGHT))

    