from circleshape import *
from constants import PLAYER_RADIUS, LINE_WIDTH
from main import *

class Player(CircleShape):
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.rotation = 0

        super().__init__(self.x, self.y, PLAYER_RADIUS)


    def triangle(self) -> list[pygame.Vector2]:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, x):
        pygame.draw.polygon(x, "white", self.triangle(), LINE_WIDTH
