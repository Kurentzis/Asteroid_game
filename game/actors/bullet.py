'''Oleg Dmitrievich Lasukov'''
import math

import arcade
from constants import *
from game.actors.flying_objects import FlyingObjects

class Bullet(FlyingObjects):
    def __init__(self, ship):
        super().__init__(PATH + r"\laserBlue01.png")
        self.radius = BULLET_RADIUS
        self.life = BULLET_LIFE
        self.ship = ship
        self.life_time = 0
        self.center.x=self.ship.center.x
        self.center.y=self.ship.center.y
        self.angle=self.ship.angle
        self.laserSXF = arcade.load_sound(PATH2+ r"\laser-blast-descend_gy7c5deo.mp3")

    
    def fire(self):
        self.velocity.dx=self.ship.velocity.dx+ BULLET_SPEED *math.cos(math.radians(self.angle))
        self.velocity.dy=self.ship.velocity.dy+ BULLET_SPEED *math.sin(math.radians(self.angle))
        self.laserSXF.play()