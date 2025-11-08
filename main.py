import pygame
from constants import *
from logger import log_state
from player import *
from stars import *


def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    Clock = pygame.time.Clock()
    dt = 0
    BLACK = (48, 25, 52)

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    star_field = Stars(SCREEN_WIDTH, SCREEN_HEIGHT)

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    player = Player(x, y)

    while True:
        log_state()
        screen.fill(BLACK)
        star_field.render_stars(screen, star_field.stars, 1, 1, (255, 255, 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        time_elapsed = Clock.tick(60)
        dt = time_elapsed / 1000
        updatable.update(dt)
        for spr in drawable:
            spr.draw(screen)
        pygame.display.flip()


if __name__ == "__main__":
    main()
