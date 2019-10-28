import random
import json
import os

from pico2d import *

import game_framework
import title_state
import pause_state

from player import Player
from enemy import Enemy
from bullet import Bullet

padWidth, padHeight = 480, 640
name = "MainState"

player = None
enemy = None
bullet = None

def enter():
    global running_game, player, enemy, bullet
    running_game = True
    open_canvas(padWidth, padHeight)
    background = load_image('background001.png')
    player = Player()
    bullet = Bullet()
    enemy = Enemy()
    pass

def exit():

    close_canvas()
    pass

def pause():
    pass


def resume():
    pass


def handle_events():
    global running_game, player, bullets, count
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_p):
            game_framework.push_state(pause_state)
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running_game = False
            elif event.key == SDLK_RIGHT:
                player.dir += 1
            elif event.key == SDLK_LEFT:
                player.dir -= 1
            elif event.key == SDLK_SPACE:
                bullet[].x = player.x
                bullet[].y = player.y + 10

        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                player.dir -= 1
            elif event.key == SDLK_LEFT:
                player.dir += 1



def update():
    player.update()
    for enemy in enemys:
        enemy.update()
    bullet.update()
    delay(0.02)

    pass

def draw():
    clear_canvas()
    player.draw()
    for enemy in enemys:
        enemy.draw()
    bullet.draw()
    update_canvas()





