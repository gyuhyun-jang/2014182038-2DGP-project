from pico2d import *
import main_state

padWidth, padHeight = 400, 600

class Background:
    def __init__(self):
        self.image = load_image('./resource/background/background_01.png')
        self.bgm = load_music('./resource/sound/bgm4.mp3')
        self.bgm.set_volume(20)
        self.bgm.repeat_play()

    def update(self):
        pass

    def draw(self):
        self.image.draw(padWidth//2, padHeight//2)
