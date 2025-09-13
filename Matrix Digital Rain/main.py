import pygame
import sys
import random
import math
import ctypes


pygame.init()
pygame.display.set_caption("Matrix Digital Rain")
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
main_bg_color = (10, 10, 13)
screen.fill(main_bg_color)

consolas_font = pygame.font.SysFont("Consolas", 20)
char_height = consolas_font.get_height()
char_width = consolas_font.size("W")[0]


def prevent_sleep():
    """ONLY FOR WINDOWS"""
    ctypes.windll.kernel32.SetThreadExecutionState(0x80000003)


def allow_sleep():
    """ONLY FOR WINDOWS"""
    ctypes.windll.kernel32.SetThreadExecutionState(0x80000000)



class FallingChar:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def change_color(self):
        time = pygame.time.get_ticks() * 0.001
        r = int(128 + 127 * math.sin(time + self.y * 0.001))
        g = int(128 + 127 * math.sin(time + 2 + self.y * 0.001))
        b = int(128 + 127 * math.sin(time + 4 + self.y * 0.001))
        return r, g, b

    def draw(self, surface):
        text_surface = consolas_font.render(
            random.choice("QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890@#№$%&<>"),
            True,
            self.change_color(),
        )
        surface.blit(text_surface, (self.x, self.y))

    def update(self):
        self.y += char_height
        return self.y <= screen.get_height()



falling_chars = []

blackout = pygame.Surface(screen.get_size(), pygame.SRCALPHA)
blackout.fill((main_bg_color[0], main_bg_color[1], main_bg_color[2], 20))

try:
    prevent_sleep()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                raise SystemExit

        pygame.time.Clock().tick(30)

        screen.blit(blackout, (0, 0))

        column_index = random.randint(0, screen.get_width() // char_width - 1)
        char_pos = column_index * char_width
        new_char = FallingChar(char_pos, -char_height)
        falling_chars.append(new_char)

        i = 0
        while i < len(falling_chars):
            if falling_chars[i].update():
                falling_chars[i].draw(screen)
                i += 1
            else:
                falling_chars.pop(i)

        pygame.display.flip()
finally:
    allow_sleep()
    pygame.quit()
    sys.exit()
