from pico2d import*
import random
import sys
from time import sleep

BLACK = (0, 0, 0)
padWidth, padHeight = 480, 640

def initGame():
    global gamePad, clock


open_canvas(padWidth, padWidth)
background = load_image('backgound001.png')
character = load_image('')
