import pygame

from constants import SCREEN_HEIGHT, SCREEN_WIDTH

VERSION = pygame.version.ver


def main():
    print(f"Starting Asteroids with pygame version: {VERSION}")


if __name__ == "__main__":
    main()
