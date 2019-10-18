from pico2d import*
import random
import sys
from time import sleep

BLACK = (0, 0, 0)
padWidth, padHeight = 480, 640


def initGame():
    global background, clock, character, running_game, x, y, state, dir
    running_game = True
    open_canvas(padWidth, padWidth)
    background = load_image('background001.png')
    character = load_image('animation01.png')
    bullet = load_image('bullet.png')
    rock = load_image('rock02.png')
    x, y, state, dir = padWidth//2, 20, 2, 0

def runGame():
    global background, clock, character, x, y, running_game, state, dir
    frame = 0
    background.draw(padWidth//2, padHeight //2)
    character.clip_draw(frame * 42, 42 * state, 42, 42, x, y)
    update_canvas()
    frame = (frame + 1) % 4
    x += dir * 5
    if (dir < 0):
        state = 0
    elif ( dir > 0 ):
        state = 1




def handle_events():
    global running_game, x, y, state, dir

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running_game = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running_game = False
            elif event.key == SDLK_RIGHT:
                dir += 1
            elif event.key == SDLK_LEFT:
                dir -= 1
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir -= 1
            elif event.key == SDLK_LEFT:
                dir += 1

initGame()

while running_game:
    runGame()
    handle_events()
    delay(0.01)

close_canvas()


