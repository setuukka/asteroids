from circleshape import CircleShape
import pygame
import random
from constants import ASTEROID_MIN_RADIUS

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

    def split(self):
        #print(f"WE ARE IN SPLIT") #DEBUG

        print(self.radius, ASTEROID_MIN_RADIUS) #DEBUG
        if self.radius <= ASTEROID_MIN_RADIUS:
            pygame.sprite.Sprite.kill(self)
            return
            
        random_angle = random.uniform(20,50)
        #print(random_angle) #DEBUG
        #print("self velocity before", self.velocity) #DEBUG

        new_angle1 = self.velocity.rotate(random_angle)
        new_angle2 = self.velocity.rotate(-random_angle)
        #print(f"{new_angle1} {new_angle2}") #DEBUG
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        #Create two new asteroids
        new_asteroid1 = Asteroid(self.position[0],self.position[1], new_radius)
        new_asteroid1.velocity = new_angle1
        new_asteroid1.velocity *= 1.2
        new_asteroid2 = Asteroid(self.position[0],self.position[1], new_radius)
        new_asteroid2.velocity = new_angle2
        new_asteroid2.velocity *= 1.2

        pygame.sprite.Sprite.kill(self)