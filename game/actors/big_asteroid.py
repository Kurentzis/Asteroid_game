'''Oleg Dmitrievich Lasukov'''
import math
import random
from constants import *
from game.actors.small_asteroid import SmallAsteroid
from game.actors.asteroid import Asteroid
from game.actors.medium_asteroid import MediumAsteroid

class BigAsteroid(Asteroid):
    def __init__(self):
        super().__init__(PATH+r"\meteorGrey_big1.png")
        self.radius = BIG_ROCK_RADIUS
        self.speed = BIG_ROCK_SPEED
        self.center.x = random.randint(1, 50)
        self.center.y = random.randint(1, 150)
        self.direction = random.randint(1, 50)
        self.velocity.dx = math.cos(math.radians(self.direction)) * self.speed
        self.velocity.dy = math.sin(math.radians(self.direction)) * self.speed
        
    def hit(self, asteroids):
        self.alive = False
        self.ifhit = 5
        self.break_into_medium_asteroid(asteroids)
        self.break_into_small_asteroid(asteroids)
        return (asteroids, self.ifhit)
    
    def break_into_medium_asteroid(self, asteroids):
        i = 0
        for i in range(2):
            ma = MediumAsteroid()
            
            ma.center.x = self.center.x
            ma.center.y = self.center.y
            
            ma.direction = self.direction
            ma.velocity.dx = self.velocity.dx
            ma.speed = self.speed
            
            if i == 0:
                ma.velocity.dy = math.sin(math.radians(self.direction+2)) * self.speed
            else:
                ma.velocity.dy = math.sin(math.radians(self.direction-2)) * self.speed
            asteroids.append(ma)
            
    def break_into_small_asteroid(self, asteroids):
        sm = SmallAsteroid()
        sm.speed = self.speed
        
        sm.center.x = self.center.x
        sm.center.y = self.center.y
        
        sm.direction = self.direction
        
        sm.velocity.dx = math.cos(math.radians(self.direction)) * self.speed + 5
        sm.velocity.dy = self.velocity.dy
        
        asteroids.append(sm)
        
    
    def rotate(self):
        self.angle += 1
        
    def score(self):
        self.ifhit = 5
        return(self.ifhit)