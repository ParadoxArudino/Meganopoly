from .page import Page
from ..settings import WIDTH, HEIGHT
import pygame

class HostSetup(Page):
    def __init__(self):
        super().__init__("Host Setup")
        pygame.display.set_caption(self.title)
    
    def run(self, screen):
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                raise SystemExit
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_F12:
                     return "fullscreen"
                           
        self.execute_render(screen)

    def execute_render(self, screen):
        self.bg_render(screen, "green")
        self.border_render(screen)

        pygame.display.flip()

        
    
    