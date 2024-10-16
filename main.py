import pygame
from constants import *
from player import *
from circleshape import *

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    #print("Starting asteroids!")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")


        player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)       
        player.draw(screen)
        pygame.display.flip()
        return_time = clock.tick(60)
        dt = return_time / 1000
    #print(f"Screen width: {SCREEN_WIDTH}")
    #print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()