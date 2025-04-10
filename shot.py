import pygame
from circleshape import*
from constants import*
from main import*

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.radius = SHOT_RADIUS

    def draw(self,screen):
        pygame.draw.circle(screen,(255,255,255),(self.position.x, self.position.y),self.radius)

    def update(self,dt):
        self.position = self.position + (self.velocity)