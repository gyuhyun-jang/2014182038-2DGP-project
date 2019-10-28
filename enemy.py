from pico2d import *
import random

class Enemy():
    def __init__(self):
        self.x, self.y = random.randint(40, 440), 639
        self.image = load_image('rock02.png')
        self.speed = random.randint(1, 3)


    def update(self):
        if self.y > 20:
            self.y -= self.speed
        else:
            self.y = 700
            pass

    def draw(self):
        self.image.draw(self.x, self.y)

    def exit(self):
        pass
