from .page import Page
import pygame

class HostSetup(Page):
    def __init__(self):
        super().__init__("Host Setup")
    
    def run(self, screen):
        self.clock = pygame.time.Clock()
        pygame.display.set_caption(self.title)

        while True:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    raise SystemExit
        
            self.execute_render(screen)
            self.clock.tick(60)

    def execute_render(self, screen):
        self.global_render(screen)

        
    
    