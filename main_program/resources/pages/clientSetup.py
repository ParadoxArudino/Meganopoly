from .page import Page
import pygame

class ClientSetup(Page):
    def __init__(self):
        super().__init__("Client Setup")
    
    def run(self, screen):
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                raise SystemExit
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_F12:
                     return "fullscreen"
                        
        self.execute_render(screen)

    def execute_render(self, screen):
        self.bg_render(screen)

        self.border_render(screen)
        pygame.display.flip()