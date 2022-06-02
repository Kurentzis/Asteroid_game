'''Oleg Dmitrievich Lasukov'''
from game.actors.flying_objects import FlyingObjects

class Asteroid(FlyingObjects):
    def __init__(self, img):
        super().__init__(img)
        self.width = self.texture.width
        self.height = self.texture.height
        self.radius = 0.0
        self.ifhit = 0

        
    def rotate(self):
        pass
        
    def hit():
        pass
    
    def score():
        pass