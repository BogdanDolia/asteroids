import sys
import pygame

from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField


def main():
    getattr(pygame, "init")()
    version = pygame.version.ver
    print(f"Starting Asteroids with pygame version: {version}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    AsteroidField()
    QUIT_EVENT = getattr(pygame, "QUIT")
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == QUIT_EVENT:
                return
        screen.fill("black")
        updatable.update(dt)
        for a in asteroids:
            for p in updatable:
                if isinstance(p, Player):
                    if a.collides_with(p):
                        log_event("player_hit")
                        print("Game over!")
                        sys.exit(0)
        for o in drawable:
            o.draw(screen)
        pygame.display.flip()
        delta_time = clock.tick(60)
        dt = delta_time / 1000
        print(f"{dt}")


if __name__ == "__main__":
    main()
