# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import*
from player import*
from circleshape import*
from asteroid import*
from asteroidfield import*
from shot import*

def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)
    
    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatable.update(dt)
        
        for a in asteroids:
            if a.collide(player):
                print("Game over!")
                return
            for s in shots:
                if a.collide(s):
                    a.split()
                    s.kill()
                    print("Asteroid destroyed!")
                    break

        screen.fill((0, 0, 0))  # Fill the screen with black
        #print("Starting Asteroids!")
        #print(f"Screen width: {SCREEN_WIDTH}")
        #print(f"Screen height: {SCREEN_HEIGHT}")
        for drawables in drawable:
            drawables.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()