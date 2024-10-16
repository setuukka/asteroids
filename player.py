from circleshape import CircleShape
import pygame
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x,y, PLAYER_RADIUS)
        self.rotation = 0
        print(f"Initial rotation: {self.rotation}") #debug print

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        #print("We are in player.py draw function")
        pygame.draw.polygon(screen, "white", self.triangle(),2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
        print(f"Rotation after update: {self.rotation}") #debug print
        #print(f"rotation {self.rotation}, turn speed {PLAYER_TURN_SPEED}, dt {dt}")

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            print("Rotating left") #Debug print
            self.rotate(-dt)  # Rotate left

        if keys[pygame.K_d]:
            print("Rotating right") #Debug print
            self.rotate(dt)   # Rotate right

        if keys[pygame.K_w]:
            self.move(dt)
        
        if keys[pygame.K_s]:
            self.move(-dt)
        

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt