import pygame
from constants import *
from player import Player
from asteroidfield import *
#from circleshape import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    #GROUPS
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroid_group = pygame.sprite.Group()

    #CONTAINERS
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroid_group)
    AsteroidField.containers = (updatable,)

    #OBJECTS
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroid_f = AsteroidField()

    dt = 0
    #print("Starting asteroids!")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return




        #player.update(dt)
        screen.fill("black")

        for thing in updatable:
            thing.update(dt)
        for other_thing in drawable:
            other_thing.draw(screen)
        #drawable.draw(screen)




        #player.draw(screen)
       

        pygame.display.flip()
        dt = clock.tick(60) / 1000



if __name__ == "__main__":
    main()