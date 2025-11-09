import pygame
from constants import *
from logger import log_state, log_event
from player import *
from stars import *
from asteroid import *
from asteroidfield import *
from shot import *
import sys


def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    Clock = pygame.time.Clock()
    dt = 0
    BLACK = (48, 25, 52)
    score = 0
    font = pygame.font.SysFont('Caskaydia Mono Nerd Font', 25)

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    star_field = Stars(SCREEN_WIDTH, SCREEN_HEIGHT)

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    asteroidfield = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    AsteroidField.containers = updatable
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    Shot.containers = (shots, updatable, drawable)


    player = Player(x, y)
    asteroidfield = AsteroidField()
    

    while True:
        log_state()
        screen.fill(BLACK)
        star_field.render_stars(screen, star_field.stars, 1, 1, (255, 255, 255))
        score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        time_elapsed = Clock.tick(60)
        dt = time_elapsed / 1000
        updatable.update(dt)
        screen.blit(score_text, (10,10))
        for astr in asteroids:
            if astr.collides_with(player) == True:
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        for astr in asteroids:
            for bullet in shots:
                if astr.collides_with(bullet):
                    log_event("asteroid_shot")
                    bullet.kill()
                    astr.split()
                    score += 1
        for spr in drawable:
            spr.draw(screen)
        pygame.display.flip()


if __name__ == "__main__":
    main()
