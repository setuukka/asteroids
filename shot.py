from circleshape import CircleShape
import pygame
from constants import SHOT_RADIUS, PLAYER_SHOOT_SPEED

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x,y, SHOT_RADIUS)
        self.position = pygame.Vector2(x,y)
        self.velocity = pygame.Vector2(0,0)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", (int(self.position.x), int(self.position.y)) ,SHOT_RADIUS, width = 2)

    def update(self, dt):
        #print(self.position) #DEBUG
        self.position += self.velocity * dt
        #self.position = self.position + (self.velocity * dt)