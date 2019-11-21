from pico2d import *

padWidth, padHeight = 400, 600


class Background:
    def __init__(self):
        self.image = load_image('./resource/background/background_01.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(padWidth//2, padHeight//2)