from pico2d import*
import random
import sys
from time import sleep

padWidth, padHeight = 480, 640

class Player:
    def __init__(self):
        self.x, self.y = padWidth // 2, 20
        self.frame = 0
        self.dir = 0
        self.image = load_image('animation01.png')

    def update(self):
        self.frame = (self.frame + 1) % 4
        self.x += self.dir * 5
        if self.dir < 0:
            self.state = 0
        elif self.dir > 0:
            self.state = 1
        elif self.dir == 0:
            self.state = 2

    def draw(self):
        self.image.clip_draw(self.frame*42, 42 * self.state, 42, 42, self.x, self.y)

class Enemy:
    def __init__(self):
        self.x, self.y = random.randint(40, 440), 639
        self.image = load_image('rock02.png')
        self.speed = 2

    def update(self):
        self.y -= self.speed

    def draw(self):
        self.image.draw(self.x, self.y)


class Bullet:
    def __init__(self):
        self.x, self.y = 0, 0
        self.image = load_image('bullet.png')
        self.speed = 10
        self.count = 0

    def update(self):
        if self.x != 0:
            self.y += self.speed

    def draw(self):
        self.image.draw(self.x, self.y)

def initGame():
    global running_game, background, clock, player, enemys, bullets, count
    running_game = True
    count = 0
    open_canvas(padWidth, padWidth)
    #background = load_image('background001.png')
    player = Player()
    enemys = [Enemy() for i in range(10)]
    bullets = [Bullet() for i in range(100)]

def runGame():
    global running_game, background, clock, player, bullets, enemys
    #background.draw(padWidth//2, padHeight //2)
    player.update()
    for enemy in enemys:
        enemy.update()
    for bullet in bullets:
        bullet.update()
    clear_canvas()
    player.draw()
    for enemy in enemys:
        enemy.draw()
    for bullet in bullets:
        bullet.draw()
    update_canvas()


def handle_events():
    global running_game, player, bullets, count

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running_game = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running_game = False
            elif event.key == SDLK_RIGHT:
                player.dir += 1
            elif event.key == SDLK_LEFT:
                player.dir -= 1
            elif event.key == SDLK_SPACE:
                bullets[count].x = player.x
                bullets[count].y = player.y + 10
                count += 1
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                player.dir -= 1
            elif event.key == SDLK_LEFT:
                player.dir += 1



initGame()
while running_game:
    runGame()
    handle_events()
    delay(0.02)


close_canvas()


