import random
import json
import os
import time

from pico2d import *

import game_framework
import title_state
import pause_state

from player import Player
from enemy import Enemy
from bullet import Bullet

padWidth, padHeight = 400, 600
name = "MainState"

player = None
enemy = None
bullet = None


def enter():
    global running_game, player, enemys, bullets, count, background
    running_game = True
    open_canvas(padWidth, padHeight)
    background = load_image('background_01.png')
    player = Player()
    enemys = [Enemy()]
    bullets = [Bullet()]
    count = 0
    pass


def exit():
    close_canvas()
    pass


def pause():
    pass


def resume():
    pass


def handle_events():
    global running_game, player, bullets, count, enemys
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
                bullets[count].x, bullets[count].y = player.x, player.y + 10
                count += 1
                if count == 20:
                    count = 0
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                player.dir -= 1
            elif event.key == SDLK_LEFT:
                player.dir += 1


def update():
    global hp, max_enemy, kill_score, max_bullet_amount
    hp = 5
    max_enemy, max_bullet_amount = 20, 20
    kill_score = 0
    player.update()
    for enemy in enemys:
        enemy.update()
    for bullet in bullets:
        bullet.update()
    # 충돌체크
    for enemy in enemys:
        if enemy.y < 30:
            if hp == 0:
                game_framework.change_state(title_state)
            hp -= 1
        for bullet in bullets:
            if enemy.x + 16 >= bullet.x >= enemy.x - 16 and enemy.y + 10 >= bullet.y >= enemy.y - 10:
                enemys.remove(enemy)
                bullets.remove(bullet)
                kill_score += 1
                break
    while len(enemys) < max_enemy:
        enemys.append(Enemy())
    while len(bullets) < max_bullet_amount:
        bullets.append(Bullet())
    if kill_score % 10 == 0:
        max_enemy += 1

    delay(0.02)
    pass


def draw():
    clear_canvas()
    background.draw(padWidth // 2, padHeight // 2)
    player.draw()
    for enemy in enemys:
        enemy.draw()
    for bullet in bullets:
        bullet.draw()
    update_canvas()
