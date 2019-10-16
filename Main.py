from pico2d import*
import random

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')
    def draw(self):
        self.image.draw(400,30)

class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100,700), 90
        self.frame = random.randint(0, 7)
        self.image = load_image('animation_sheet.png')
    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5
    def draw(self):
        self.image.clip_draw(self.frame* 100, 100, 100, 100, self.x, self.y)

class Ball:
    def __init__(self):
        self.x, self.y = random.randint(0,800), 599
        self.image_small = load_image('ball21x21.png')
        self.speed = random.randint(5,10)

    def update(self):
        if self.y < 65:
            self.y = 65
        else:
            self.y -= self.speed
    def draw(self):
        self.image_small.draw(self.x,self.y)

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

open_canvas()
boy = Boy()
balls = [Ball() for i in range(20)]
grass = Grass()
running = True

while running:
    handle_events()
    boy.update()
    for ball in balls:
        ball.update()
    clear_canvas()
    grass.draw()
    boy.draw()
    for ball in balls:
        ball.draw()
    update_canvas()
    delay(0.05)


close_canvas()
