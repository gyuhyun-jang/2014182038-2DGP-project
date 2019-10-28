from pico2d import*

class Bullet:
    def __init__(self):
        self.x, self.y = 0, 0
        self.image = load_image('bullet.png')
        self.speed = 10
        self.count = 0

    def update(self):
        if self.x != 0:
            self.y += self.speed
            if(self.y > 680):
                del(self)

    def draw(self):
        self.image.draw(self.x, self.y)