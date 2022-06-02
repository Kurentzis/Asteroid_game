'''Oleg Dmitrievich Lasukov'''
from constants import *
from game.actors.asteroid import Asteroid

class SmallAsteroid(Asteroid):
    def __init__(self):
        super().__init__(PATH+r"\meteorGrey_small1.png")
        self.radius = SMALL_ROCK_RADIUS
    def hit(self, asteroids):
        self.alive = False

    def rotate(self):
        self.angle += 5
        
    def score(self):
        self.ifhit = 2
        return(self.ifhit)