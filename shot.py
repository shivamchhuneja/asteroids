from circleshape import *
import pygame
from constants import *


class Shot(CircleShape):
    def __init__(self, x, y, angle):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = pygame.Vector2(0, 1).rotate(angle) * PLAYER_SHOOT_SPEED

    def draw(self, screen):
        WHITE = (255, 255, 255)
        pygame.draw.circle(screen, WHITE, self.position, SHOT_RADIUS, width=2)

    def update(self, dt):
        self.position += self.velocity * dt
