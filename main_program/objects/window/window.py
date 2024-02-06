import pygame
import pygame._sdl2 as sdl2

from main_program.settings import WIDTH, HEIGHT

pygame.init()

class Window:
    def __init__(self) -> None:
        pygame.display.set_mode((WIDTH, HEIGHT), pygame.SCALED | pygame.RESIZABLE | pygame.HIDDEN)
        
        self.window = sdl2.Window.from_display_module()
        self.window.size = (WIDTH, HEIGHT)
        self.window.position = sdl2.WINDOWPOS_CENTERED
        self.window.show()

        self.screen = pygame.display.get_surface()
    
    def run(self, page):
        page.run(self.screen)
