from circleshape import CircleShape
import pygame

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self, screen):
        #print(f"Asteroid DRAW called with {self.x},{self.y}") #DEBUG
        #pygame.draw.circle(screen, "white", [self.x, self.y],self.radius, width = 2)
        pygame.draw.circle(screen, "white", self.position ,self.radius, width = 2)


    def update(self, dt):
        #print(self.position) #DEBUG
        #self.position = self.position+self.velocity + (self.velocity * dt)
        self.position = self.position + (self.velocity * dt)
