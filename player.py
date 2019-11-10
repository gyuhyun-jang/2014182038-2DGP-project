from pico2d import*

padWidth,padHeight = 400,600

class Player:
    def __init__(self):
        self.x, self.y = padWidth // 2, 20
        self.frame = 0
        self.dir = 0
        self.image = load_image('animation01.png')

    def update(self):
        self.frame = (self.frame + 1) % 4
        self.x += self.dir * 5
        self.x = clamp(20,self.x,380)
        if self.dir < 0:
            self.state = 0
        elif self.dir > 0:
            self.state = 1
        elif self.dir == 0:
            self.state = 2

    def draw(self):
        self.image.clip_draw(self.frame*42, 42 * self.state, 42, 42, self.x, self.y)
