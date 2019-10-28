from pico2d import *


class Bullet:
    def __init__(self):
        self.x, self.y = 0, 0
        self.image = load_image('bullet.png')
        self.speed = 10

    def update(self):
        self.y += self.speed

    def draw(self):
        self.image.draw(self.x, self.y)