'''Oleg Dmitrievich Lasukov'''
import random 
from constants import *
from game.actors.flying_objects import FlyingObjects

    
class Fuel(FlyingObjects):
    def __init__(self):
        super().__init__(PATH+r"\Fuel_depot_ME2.png")
        self.center.x = random.randint(1, SCREEN_WIDTH)
        self.center.y = random.randint(1, SCREEN_HEIGHT)
        self.speed = 0
        self.radius = 50
    
    def rotate(self):
        self.angle += 1