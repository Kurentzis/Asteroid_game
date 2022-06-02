'''Oleg Dmitrievich Lasukov'''
import math

import arcade
from constants import *
from game.actors.flying_objects import FlyingObjects

class Ship(FlyingObjects):
    def __init__(self):
        super().__init__(PATH+r"\ship.png")
        self.center.x = SCREEN_WIDTH/2
        self.center.y = SCREEN_HEIGHT/2
        self.radius = 40
        self.angle = 0
        self.velocity.dx = 0
        self.velocity.dy = 0
        self.lives = 3
        self.ifhit = 0
        
        
        
    def left(self):
        self.angle += SHIP_TURN_AMOUNT
        
    
    def right(self):
        self.angle -= SHIP_TURN_AMOUNT
    
    def forward(self):
        self.velocity.dx += SHIP_THRUST_AMOUNT * math.cos(math.radians(self.angle))
        self.velocity.dy += SHIP_THRUST_AMOUNT * math.sin(math.radians(self.angle))
    
    def backward(self):
        self.velocity.dx -= SHIP_THRUST_AMOUNT * math.cos(math.radians(self.angle))
        self.velocity.dy -= SHIP_THRUST_AMOUNT * math.sin(math.radians(self.angle))