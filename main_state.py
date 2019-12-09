import json
import os

from pico2d import *
import game_world
import game_framework
import dead_state
import pause_state

from player import Player
from enemy import Enemy
from background import Background
from UI import UI_Manager

padWidth, padHeight = 400, 600
name = "MainState"

player = None
player_life = 0

enemy = None
enemys = []
max_amount_of_enemys = 0
did_you_make_enemy = True
enemy_life = 0
boss_life = 0
skill_time = 0
skill_cooldown = 0
cooldown_timer = False

UI = None

bullet_damage = 0

font = None
background = None

time = 0
time_start_sign = False
kill_score = 0
money = 0
upgrade_cost = 0

def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False
    return True


def enter():
    global running_game, time, time_start_sign, player_life, bullet_damage, \
        did_you_make_enemy, upgrade_cost, money, skill_time, skill_cooldown, cooldown_timer
    running_game = True
    time = 0
    time_start_sign = True
    player_life = 5
    bullet_damage = 1
    did_you_make_enemy = True
    upgrade_cost = 20
    skill_time = 2
    skill_cooldown = 30
    cooldown_timer = True

    global player
    player = Player()
    game_world.add_object(player, 1)

    global enemys, max_amount_of_enemys, kill_score, enemy_life
    kill_score, max_amount_of_enemys, enemy_life = 0, 5, 1
    money = kill_score
    enemys = [Enemy() for i in range(max_amount_of_enemys)]
    game_world.add_objects(enemys, 1)


    global UI
    UI = UI_Manager()
    game_world.add_object(UI, 1)

    global background
    background = Background()
    game_world.add_object(background, 0)


def exit():
    game_world.clear()


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
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            game_framework.push_state(pause_state)
        else:
            player.handle_event(event)


def update():
    global enemy,enemys, max_amount_of_enemys, kill_score, time, player_life,\
        boss_life, did_you_make_enemy, enemy_life, money, skill_cooldown, cooldown_timer
    for game_object in game_world.all_objects():
        game_object.update()
    if time_start_sign:
        time += game_framework.frame_time * 1
    if did_you_make_enemy == False and kill_score % 10 == 0:
        if kill_score % 15 == 0:
            enemy_life += 1
        max_amount_of_enemys += 1
        enemy = Enemy()
        enemys.append(enemy)
        game_world.add_object(enemy, 1)
        did_you_make_enemy = True
    if kill_score % 10 == 1:
        did_you_make_enemy = False
    if player_life <= 0:
        game_world.clear()
        game_framework.change_state(dead_state)
    if cooldown_timer is True:
        skill_cooldown -= game_framework.frame_time



def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()
