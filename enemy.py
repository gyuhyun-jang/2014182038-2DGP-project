from pico2d import *
import random
from bullet import Bullet

rockimage = ['rock02.png','rock14.png','rock18.png']

class Enemy():
    def __init__(self):
        self.x, self.y = random.randint(40, 370), 640
        self.image = load_image(rockimage[random.randint(0,2)])
        self.speed = random.randint(1, 3)
        self.hp = 10

    def update(self):
        if self.y > 20:
            self.y -= self.speed
        elif self.y < 40:
            self.x, self.y = random.randint(30, 370), 640
            self.speed = random.randint(1, 3)


    def draw(self):
        self.image.draw(self.x, self.y)

    def exit(self):
        pass

