from circleshape import *
import pygame
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
    
    def draw(self, screen):
        WHITE = (255, 255, 255)
        pygame.draw.circle(screen, WHITE, self.position, SHOT_RADIUS, width=2)

    def update(self, dt):
        mid = self.velocity * dt
        self.position += mid


