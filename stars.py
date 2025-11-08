import pygame
import random
from constants import SCREEN_WIDTH, SCREEN_HEIGHT


class Stars:
    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        self.stars = []
        self.num_stars = 100

        for _ in range(self.num_stars):
            x = random.randint(0, SCREEN_WIDTH)
            y = random.randint(0, SCREEN_HEIGHT)
            self.stars.append((x, y))

    def render_stars(self, surface, stars, speed, size, color):
        for star in stars:
            star_y = star[1] + speed
            if star_y > SCREEN_HEIGHT:
                star_y = 0

            pygame.draw.circle(surface, color, (star[0], star_y), size)
