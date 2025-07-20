from circleshape import CircleShape 
from constants import ASTEROID_MIN_RADIUS, PLAYER_RADIUS, PLAYER_SPEED, PLAYER_TURN_SPEED
import pygame
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, 'white', self.position, self.radius, 2)
        
    def update(self, dt):
        self.position += self.velocity*dt
    
    def split(self):
        self.kill()
        
        # if it's a small one just return, you've completely killed it
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        # get a new random direction for each of the two new asteroids
        angle = random.uniform(20,50)
        new_vec_pos = self.velocity.rotate(angle)
        new_vec_neg = self.velocity.rotate(-1*angle)
        
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        
        asteroid1 = Asteroid(self.position[0], self.position[1], new_radius)
        asteroid2 = Asteroid(self.position[0], self.position[1], new_radius)
        asteroid1.velocity = new_vec_pos*1.2
        asteroid2.velocity = new_vec_neg*1.2
        
        