from typing import Self
import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        raise NotImplementedError

    def update(self, dt):
        raise NotImplementedError

    def has_collided_with(self, circle_shape: Self):
        distance = self.position.distance_to(circle_shape.position)

        if distance <= self.radius + circle_shape.radius:
            return True
        return False
