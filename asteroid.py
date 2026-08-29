import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def split(self, screen):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        log_event("asteroid_split")
        rng = random.uniform(20, 50)

        vel_1 = self.velocity.rotate(rng)
        vel_2 = self.velocity.rotate(-rng)

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        new_asteroid_1 = Asteroid(self.position[0], self.position[1], new_radius)
        new_asteroid_1.velocity = 1.2*vel_1

        new_asteroid_2 = Asteroid(self.position[0], self.position[1], new_radius)
        new_asteroid_2.velocity = 1.2*vel_2


    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt
