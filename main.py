# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import*
from player import*
from circleshape import*

def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    dt = 0
    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        player.update(dt)
        screen.fill((0, 0, 0))  # Fill the screen with black
        #print("Starting Asteroids!")
        #print(f"Screen width: {SCREEN_WIDTH}")
        #print(f"Screen height: {SCREEN_HEIGHT}")
        player.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()