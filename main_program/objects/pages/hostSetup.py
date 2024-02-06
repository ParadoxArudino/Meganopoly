from .page import Page

class HostSetup(Page):
    def __init__(self):
        super().__init__("Host Setup")
    
    def run(self, screen):
        while True:
            self.execute_render(screen)

    def execute_render(self, screen):
        self.global_render(screen)
        
    
    