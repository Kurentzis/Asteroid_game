'''Oleg Dmitrievich Lasukov'''
import arcade
import math
from constants import *
from abc import ABC, abstractmethod 
from game.actors.point import Point
from game.actors.velocity import Velocity


class FlyingObjects():
    def __init__(self, img):
        self.center = Point()
        self.velocity = Velocity()
        self.alive = True
        self.img = img
        self.texture = arcade.load_texture(self.img)
        self.width = self.texture.width
        self.height = self.texture.height
        self.radius = SHIP_RADIUS
        self.angle = 0
        self.speed = 1
        self.direction = 1
        self.velocity.dx = math.cos(math.radians(self.direction)) * self.speed
        self.velocity.dy = math.sin(math.radians(self.direction)) * self.speed
 
    def advance(self):
        self.center.x += self.velocity.dx
        self.center.y += self.velocity.dy
   
    def is_alive(self):
        return self.alive

    def draw(self):
        arcade.draw_texture_rectangle(self.center.x, self.center.y, self.width, self.height, self.texture, self.angle, 255)
   
    def wrap(self):
        if self.center.x-SHIP_RADIUS > SCREEN_WIDTH:
            self.center.x = -SHIP_RADIUS
        if self.center.y-SHIP_RADIUS > SCREEN_HEIGHT:
            self.center.y = -SHIP_RADIUS
        if self.center.x+SHIP_RADIUS < 0:
            self.center.x = SCREEN_WIDTH+SHIP_RADIUS
        if self.center.y+SHIP_RADIUS < 0:
            self.center.y = SCREEN_HEIGHT+SHIP_RADIUS
            
    @abstractmethod
    def fire(self):
        pass