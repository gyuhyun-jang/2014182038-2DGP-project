from pico2d import *
import random
import game_framework
import game_world
import main_state
PIXEL_PER_METER = (10.0 / 0.5)  # 10 pixel 50 cm
RUN_SPEED_KMPH = 10.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)


enemy_type = ['./resource/enemy/rock0_0.png', './resource/enemy/rock0_1.png', './resource/enemy/rock0_2.png',
              './resource/enemy/rock1_0.png', './resource/enemy/rock1_1.png', './resource/enemy/rock1_2.png',
              './resource/enemy/rock2_0.png', './resource/enemy/rock2_1.png', './resource/enemy/rock2_2.png']
enemy_size = [60, 50, 40]


class Enemy:
    image = None
    explosion_image = None

    def __init__(self):
        if Enemy.image is None:
            self.image = load_image(enemy_type[random.randint(0, 2)])
            self.explosion_image = load_image('./resource/explosion.png')
            self.size = enemy_size[0]
        self.x, self.y = random.randint(40, 370), 640
        self.fall_speed = RUN_SPEED_PPS
        self.hp = main_state.enemy_life
        self.explosion_sound = load_wav('./resource/sound/explosion.wav')
        self.explosion_sound.set_volume(2)


    def get_bb(self):
        return self.x - self.size//2, self.y - self.size//2, self.x + self.size, self.y + self.size

    def update(self):
        self.y -= self.fall_speed * game_framework.frame_time

        if self.y < 0:
            self.explosion_sound.play()
            main_state.player_life -= 1
            self.hp = main_state.enemy_life
            main_state.kill_score += 1
            self.x, self.y = random.randint(40, 370), 640

        if self.hp <= 0:
            self.explosion_sound.play()
            self.hp = main_state.enemy_life
            main_state.kill_score += 1
            self.x, self.y = random.randint(40, 370), 640
            main_state.money += 1

    def draw(self):
        if self.hp <= 0:
            self.explosion_image.draw(self.x, self.y)
        else:
            self.image.draw(self.x, self.y)

    def exit(self):
        pass

