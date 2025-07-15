import pygame
from constants import *

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids Game")
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))  # Clear the screen with black
        pygame.display.flip()  # Update the display
        clock.tick(60)  # Limit to 60 FPS
        print(f"Asteroid spawn rate: {ASTEROID_SPAWN_RATE} seconds")
        print(f"Asteroid max radius: {ASTEROID_MAX_RADIUS}")
        print(f"Asteroid kinds: {ASTEROID_KINDS}")
        print(f"Asteroid min radius: {ASTEROID_MIN_RADIUS}")
    pygame.quit()

if __name__ == "__main__":
    main()
