import pygame
from constants import EXPLOSION_DURATION, EXPLOSION_RADIUS


class Explosion(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        super().__init__()
        self.position = pygame.Vector2(x, y)
        self.radius = radius
        self.age = 0
        self.duration = EXPLOSION_DURATION
        self.start_radius = radius * 1.5
        self.max_radius = radius * 3

    def update(self, dt):
        self.age += dt
        if self.age >= self.duration:
            self.kill()

    def draw(self, screen):
        if self.age >= self.duration:
            return

        # Calculate animation progress (0 to 1)
        progress = self.age / self.duration

        # Expand and fade effect
        current_radius = self.start_radius + (self.max_radius - self.start_radius) * progress

        # Fade out the alpha (opacity)
        alpha = int(255 * (1 - progress))

        # Draw expanding circles for explosion effect
        colors = [
            (255, 165, 0),  # Orange
            (255, 100, 0),  # Dark orange
            (255, 50, 0),   # Red-orange
        ]

        for i, color in enumerate(colors):
            offset = self.start_radius + (self.max_radius - self.start_radius) * progress * (1 - i * 0.2)
            # Draw circle with fading effect
            surface = pygame.Surface((int(offset * 2), int(offset * 2)), pygame.SRCALPHA)
            pygame.draw.circle(
                surface,
                (*color, alpha),
                (int(offset), int(offset)),
                int(offset)
            )
            screen.blit(surface, (self.position.x - offset, self.position.y - offset))
