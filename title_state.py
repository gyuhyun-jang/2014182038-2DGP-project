import game_framework
import main_state
from pico2d import *


name = "TitleState"
image = None


def enter():
    global image
    open_canvas(510,600)
    image = load_image('kpu_credit.png')


def exit():
    global image
    del(image)


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if(event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif(event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                game_framework.change_state(main_state)


def draw():
    clear_canvas()
    image.draw(510 // 2, 600 // 2)
    update_canvas()

def update():
    pass

def pause():
    pass

def resume():
    pass






