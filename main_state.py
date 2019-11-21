import random
import json
import os
import time

from pico2d import *
import game_world
import game_framework
import title_state
import pause_state

from player import Player
from enemy import Enemy
from bullet import Bullet
from background import Background

padWidth, padHeight = 400, 600
name = "MainState"

player = None
enemy = None
bullet = None
enemys = []
kill_score = 0


def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True


def get_player():
    return player


def get_bullet():
    return bullet


def enter():
    global running_game
    running_game = True

    global player
    player = Player()
    game_world.add_object(player, 1)


    global enemys, amount_of_enemys
    amount_of_enemys = 20
    enemys = [Enemy() for i in range(amount_of_enemys)]
    game_world.add_objects(enemys, 1)

    background = Background()
    game_world.add_object(background, 0)


def exit():
    game_world.clear()
    pass


def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_Quit:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            player.handle_event(event)


def update():
    for game_object in game_world.all_objects():
        game_object.update()
    for enemy in enemys:
        if collide(bullet, enemy):
            bullet.hit_enemy()
            enemy.get_damaged(bullet.damage)




def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()

