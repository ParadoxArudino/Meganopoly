import pygame
import pygame._sdl2 as sdl2

WIDTH, HEIGHT = (720, 480)
pygame.init()

class Window:
    def __init__(self) -> None:
        pygame.display.set_mode((WIDTH, HEIGHT), pygame.SCALED | pygame.RESIZABLE | pygame.HIDDEN)
        
        self.window = sdl2.Window.from_display_module()
        self.window.size = (WIDTH, HEIGHT)
        self.window.position = sdl2.WINDOWPOS_CENTERED
        self.window.show()

        self.screen = pygame.display.get_surface()

        renderer = sdl2.Renderer.from_window(self.window)
        renderer.draw_color = pygame.Color("blue")
        self.clock = pygame.time.Clock()
    
    def Run(self):
        while True:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    raise SystemExit
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_F12:
                        pygame.display.toggle_fullscreen()
                        self.window.size = (WIDTH, HEIGHT)
            
            self.screen = pygame.display.get_surface()
            self.screen.fill("black")

            self.execute_render()

            pygame.display.flip()
            self.clock.tick(60)
    
    def execute_render(self):
        self.screen.fill("black")
        self.draw_border()
        
    def draw_border(self):
        pygame.draw.rect(self.screen, "blue", (0, 0, WIDTH, 10))
        pygame.draw.rect(self.screen, "blue", (0, HEIGHT-10, WIDTH, 10))
        pygame.draw.rect(self.screen, "blue", (0, 0, 10, HEIGHT))
        pygame.draw.rect(self.screen, "blue", (WIDTH-10, 0, 10, HEIGHT))