'''Oleg Dmitrievich Lasukov'''
import math
from constants import *
from game.actors.small_asteroid import SmallAsteroid
from game.actors.asteroid import Asteroid

class MediumAsteroid(Asteroid):
    def __init__(self):
        super().__init__(PATH+r"\meteorGrey_med1.png")
        self.img = "meteorGrey_med1.png"
        self.radius = MEDIUM_ROCK_RADIUS
        self.velocity.dx = math.cos(math.radians(self.direction)) * self.speed
        self.velocity.dy = math.sin(math.radians(self.direction)) * self.speed
        
    def hit(self, asteroids):
        self.alive = False
        i = 0
        self.ifhit = 3
        for i in range(2):
            sm = SmallAsteroid()
            sm.speed = self.speed
            sm.center.x = self.center.x
            sm.center.y = self.center.y
            sm.direction = self.direction
            if i == 0:
                sm.velocity.dx = math.cos(math.radians(self.direction+1.5)) * self.speed
                sm.velocity.dy = math.sin(math.radians(self.direction+1.5)) * self.speed
            else:
                sm.velocity.dy = math.sin(math.radians(self.direction-1.5)) * self.speed
                sm.velocity.dx = math.cos(math.radians(self.direction-1.5)) * self.speed
            asteroids.append(sm)
        return (asteroids, self.ifhit)
    
    def rotate(self):
        self.angle -= 2
        
    def score(self):
        self.ifhit = 3
        return(self.ifhit)