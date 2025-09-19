import pygame
import random
import math
import os


pygame.init()

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
SCREEN_WIDTH, SCREEN_HEIGHT = screen.get_size()

pygame.display.set_caption("Matrix Digital Rain")
main_bg_color = (10, 10, 13)
screen.fill(main_bg_color)

base_path = os.path.dirname(os.path.abspath(__file__))
font_path = os.path.join(base_path, "Roboto_font.ttf")
consolas_font = pygame.font.Font(font_path, 20)

char_height = consolas_font.get_height()
char_width = consolas_font.size("W")[0]



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
            False,
            self.change_color(),
        )
        surface.blit(text_surface, (self.x, self.y))

    def update(self):
        self.y += char_height
        return self.y <= SCREEN_HEIGHT



def main():
    falling_chars = []

    blackout = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
    blackout.fill((main_bg_color[0], main_bg_color[1], main_bg_color[2], 20))

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        clock.tick(30)

        screen.blit(blackout, (0, 0))

        if len(falling_chars) < 100:  # Ограничиваем количество символов
            column_index = random.randint(0, SCREEN_WIDTH // char_width - 1)
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


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        pygame.quit()
        raise
