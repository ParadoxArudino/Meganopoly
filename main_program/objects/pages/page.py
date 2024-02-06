from settings import WIDTH, HEIGHT, BG_COLOUR
import pygame

class Page:
    def __init__(self, title, border = True) -> None:
        self.title = title
        self.border = border
    
    def global_render(self, screen):
        screen.fill(BG_COLOUR)
        self.draw_border(screen, (255, 255, 255))

    def draw_border(self, screen, colour):
        pygame.draw.rect(screen, colour, (0, 0, WIDTH, 10))
        pygame.draw.rect(screen, colour, (0, HEIGHT-10, WIDTH, 10))
        pygame.draw.rect(screen, colour, (0, 0, 10, HEIGHT))
        pygame.draw.rect(screen, colour, (WIDTH-10, 0, 10, HEIGHT))

    