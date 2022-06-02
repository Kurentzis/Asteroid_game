'''Oleg Dmitrievich Lasukov'''
import math
from constants import *
from game.actors.flying_objects import FlyingObjects


class LaserReaper(FlyingObjects):
    def __init__(self, reaper):
        super().__init__(PATH+r"\234334188055212.png")
        self.radius = 50
        self.life = BULLET_LIFE
        self.life_time = 0
        self.reaper = reaper
        self.center.x=self.reaper.center.x
        self.center.y=self.reaper.center.y
        self.angle=self.reaper.angle - 40

    
    def fire(self):
        
        self.velocity.dx=self.reaper.velocity.dx+ BULLET_SPEED *math.cos(math.radians(self.angle))
        self.velocity.dy=self.reaper.velocity.dy+ BULLET_SPEED *math.sin(math.radians(self.angle))
            