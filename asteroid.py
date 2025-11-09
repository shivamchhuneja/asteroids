from circleshape import *
from constants import *
from logger import *
import random
import pygame


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        WHITE = (255, 255, 255)
        pygame.draw.circle(screen, WHITE, self.position, self.radius, width=2)

    def update(self, dt):
        mid = self.velocity * dt
        self.position += mid

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            angle = random.uniform(20, 50)
            v1 = self.velocity.rotate(angle) * 1.2
            v2 = self.velocity.rotate(-angle) * 1.2
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            ast1 = Asteroid(self.position.x, self.position.y, new_radius)
            ast2 = Asteroid(self.position.x, self.position.y, new_radius)
            ast1.velocity = v1
            ast2.velocity = v2
