import pygame
import pygame._sdl2 as sdl2

from ..settings import WIDTH, HEIGHT, OUTER_FILL_COLOR


pygame.init()

class Window:
    def __init__(self) -> None:
        pygame.display.set_mode((WIDTH, HEIGHT), pygame.SCALED | pygame.RESIZABLE | pygame.HIDDEN)
        
        self.window = sdl2.Window.from_display_module()
        self.window.size = (WIDTH, HEIGHT)
        self.window.position = sdl2.WINDOWPOS_CENTERED
        self.window.show()

        renderer = sdl2.Renderer.from_window(self.window)
        renderer.draw_color = pygame.Color(OUTER_FILL_COLOR)

        self.screen = pygame.display.get_surface()
    
    def run(self, page):
        self.clock = pygame.time.Clock()
        while True:
            cmd = page.run(self.screen)

            if cmd == "fullscreen":
                pygame.display.toggle_fullscreen()
                self.window.size = (WIDTH, HEIGHT)            

            self.clock.tick(60)

