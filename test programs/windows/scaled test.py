import pygame
import pygame._sdl2 as sdl2

pygame.init()

WIDTH, HEIGHT = (720, 480)
flags = pygame.SCALED
flags |= pygame.RESIZABLE  # optional

# create the display in "hidden" mode, because it isn't properly sized yet
pygame.display.set_mode((WIDTH, HEIGHT), flags | pygame.HIDDEN)

# choose the initial scale factor for the window
initial_scale_factor = 1  # <-- adjustable
window = sdl2.Window.from_display_module()
window.size = (WIDTH * initial_scale_factor, HEIGHT * initial_scale_factor)
window.position = sdl2.WINDOWPOS_CENTERED
window.show()

# bonus: specify the color of the out-of-bounds area in RESIZABLE mode (it's black by default)
OUTER_FILL_COLOR = "blue"
renderer = sdl2.Renderer.from_window(window)
renderer.draw_color = pygame.Color(OUTER_FILL_COLOR)

clock = pygame.time.Clock()

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            raise SystemExit
    screen = pygame.display.get_surface()
    screen.fill("black")

    t = pygame.time.get_ticks() / 1000
    pygame.draw.circle(screen, "gray40", ((30 * t) % WIDTH, (20 * t) % HEIGHT), 16)
    pygame.draw.circle(screen, "gray50", ((-20 * t) % WIDTH, (30 * t) % HEIGHT), 24)
    pygame.draw.circle(screen, "gray60", ((100 + 50 * t) % WIDTH, (30 - 10 * t) % HEIGHT), 32)

    pygame.display.flip()
    clock.tick(60)