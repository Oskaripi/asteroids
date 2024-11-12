import pygame
from constants import *
from player import *
from circleshape import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = (updatable,)
    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0, 0, 0))
        dt = clock.tick(60) / 1000
        for i in drawable:
            i.draw(screen)
        for i in updatable:
            i.update(dt)
        for i in asteroids:
            if player.collisions(i) == True:
                print("Game Over!")
                exit()
        for i in asteroids:
            for s in shots:
                if s.collisions(i) == True:
                    i.split()

        pygame.display.flip()

if __name__ == "__main__":
    main()