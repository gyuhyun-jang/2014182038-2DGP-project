import game_framework
import main_state
from pico2d import *
import title_state


name = "DeadState"
image = None
sound = None

def enter():
    global image, sound
    image = load_image('./resource/dead_state.png')
    sound = load_music('./resource/sound/gameover.wav')
    sound.set_volume(20)
    sound.play()

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
                game_framework.change_state(title_state)


def draw():
    clear_canvas()
    image.draw(400 // 2, 600 // 2)
    update_canvas()

def update():
    pass

def pause():
    pass

def resume():
    pass






