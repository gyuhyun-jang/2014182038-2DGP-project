from pico2d import *
import random
import game_framework
import game_world

PIXEL_PER_METER = (10.0 / 0.5)  # 10 pixel 50 cm
RUN_SPEED_KMPH = 20.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

SPEED_INCREASE = 1.0

enemy_type = ['./resource/enemy/rock02.png',
              './resource/enemy/rock14.png',
              './resource/enemy/rock18.png']


class Enemy():
    image = None

    def __init__(self):
        if Enemy.image == None:
            self.image = load_image(enemy_type[0])
        self.x, self.y, self.fall_speed = random.randint(40, 370), 640, RUN_SPEED_PPS * SPEED_INCREASE
        self.hp = 1


    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def update(self):
        self.y -= self.fall_speed * game_framework.frame_time

        if self.y < 0:
            game_world.remove_object(self)

        if self.hp <= 0:
            game_world.remove_object(self)

    def draw(self):
        self.image.draw(self.x, self.y)

    def get_damaged(self, x):
        self.hp -= x

    def exit(self):
        pass

