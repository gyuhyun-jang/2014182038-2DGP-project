from pico2d import *
from resource import *
import resource

class Bullet:
    def __init__(self):
        self.x, self.y = 0, 0
        self.image = load_image('bullet.png')
        self.speed = 12

    def update(self):
        if self.x != 0:
            self.y += self.speed

    def draw(self):
        self.image.draw(self.x, self.y)