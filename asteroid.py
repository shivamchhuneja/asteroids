from circleshape import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        WHITE = (255, 255, 255)
        pygame.draw.circle(screen, WHITE, self.position, self.radius, width=2)

    def update(self, dt):
        mid = self.velocity * dt
        self.position += mid
