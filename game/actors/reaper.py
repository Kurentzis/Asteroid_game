'''Oleg Dmitrievich Lasukov'''
import arcade
import math
import random 
from constants import *
from game.actors.flying_objects import FlyingObjects
from game.actors.ship import Ship
from game.actors.bullet import Bullet


class Reaper(FlyingObjects):
    def __init__(self):
        super().__init__(PATH+r"\Sovereign_charshot.png")
        self.center.x = random.uniform(30, 100)
        self.center.y = random.uniform(30, 800)
        self.radius = 50
        self.speed = 1
        self.ship = Ship()
        self.bullet = Bullet(self.ship)
        self.angle = 0
        self.lives = 3
        self.direction = self.ship.center
        self.bullet_img = arcade.load_texture(PATH+r"\234334188055212.png")
        
        self.velocity.dx = self.speed * math.cos(math.radians(self.angle))
        self.velocity.dy = self.speed * math.sin(math.radians(self.angle))

        
    def hit(self):
        self.ifhit = 0
        self.ifhit += 1
        self.lives -= 1
        self.if_alive()
        return(self.ifhit)
        

    def if_alive(self):
        if self.lives == 0:
            self.alive = False
            self.ifhit += 5
        return (self.ifhit)  