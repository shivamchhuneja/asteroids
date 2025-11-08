from circleshape import *
from constants import *


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.x = x
        self.y = y
        self.rotation = 0

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        points = self.triangle()
        WHITE = (255, 255, 255)
        pygame.draw.polygon(screen, WHITE, points, width=2)

    def rotate(self, dt):
        delta_rotation = PLAYER_TURN_SPEED * dt
        self.rotation += delta_rotation

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)

        self.move(dt)

    def move(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            forward = pygame.Vector2(0, 1).rotate(self.rotation)
            self.position += forward * PLAYER_SPEED * dt
        if keys[pygame.K_s]:
            backward = pygame.Vector2(0, 1).rotate(self.rotation)
            self.position += backward * PLAYER_SPEED * -dt
