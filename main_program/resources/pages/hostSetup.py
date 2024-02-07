from .page import Page
from ..settings import WIDTH, HEIGHT
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
        self.bg_render(screen)

        t = pygame.time.get_ticks() / 1000
        pygame.draw.circle(screen, "gray40", ((30 * t) % WIDTH, (20 * t) % HEIGHT), 16)
        pygame.draw.circle(screen, "gray50", ((-20 * t) % WIDTH, (30 * t) % HEIGHT), 24)
        pygame.draw.circle(screen, "gray60", ((100 + 50 * t) % WIDTH, (30 - 10 * t) % HEIGHT), 32)

        self.border_render(screen)

        pygame.display.flip()

        
    
    