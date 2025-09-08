import pygame
import sys
import random
import math

pygame.init()
pygame.display.set_caption("Matrix Digital Rain")
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
main_bg_color = (10, 10, 13)
screen.fill(main_bg_color)

consolas_font = pygame.font.SysFont("Consolas", 18)



class FallingChar:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        time = pygame.time.get_ticks() * 0.001
        self.R = int(128 + 127 * math.sin(time))
        self.G = int(128 + 127 * math.sin(time + 2))
        self.B = int(128 + 127 * math.sin(time + 4))

    def draw(self, surface):
        text_surface = consolas_font.render(
        random.choice("QWERTYUIOPASDFGHJKLZXCVBNM qwertyuiopasdfghjklzxcvbnm 1234567890 @#№$%&<>"),
        True,
        (self.R, self.G, self.B)
        )
        surface.blit(text_surface, (self.x, self.y))

    def update(self):
        self.y += consolas_font.get_height()
        return self.y <= screen.get_height()



falling_chars = []

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit()

    pygame.time.Clock().tick(30)

    blackout = pygame.Surface((screen.get_width(), screen.get_height()), pygame.SRCALPHA)
    blackout.fill((main_bg_color[0], main_bg_color[1], main_bg_color[2], 20))
    screen.blit(blackout, (0, 0))

    column_index = random.randint(0, screen.get_width() // consolas_font.get_height())
    char_pos = column_index * consolas_font.get_height()
    new_char = FallingChar(char_pos, -100)
    falling_chars.append(new_char)

    falling_chars = [char for char in falling_chars if char.update()]
    for char in falling_chars:
        char.draw(screen)

    pygame.display.flip()
