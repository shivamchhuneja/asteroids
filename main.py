import pygame
from constants import *
from logger import log_state, log_event
from player import *
from stars import *
from asteroid import *
from asteroidfield import *
import sys


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
    asteroids = pygame.sprite.Group()
    asteroidfield = pygame.sprite.Group()

    AsteroidField.containers = updatable
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)

    player = Player(x, y)
    asteroidfield = AsteroidField()

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
        for astr in asteroids:
            if astr.collides_with(player) == True:
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        for spr in drawable:
            spr.draw(screen)
        pygame.display.flip()


if __name__ == "__main__":
    main()
