from pico2d import *
import game_world
import game_framework
import enemy
import player
import main_state


PIXEL_PER_METER = (10.0 / 0.5)  # 10 pixel 50 cm
RUN_SPEED_KMPH = 0.1  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)


class Bullet:
    image = None

    def __init__(self):
        if Bullet.image is None:
            Bullet.image = load_image('./resource/bullet.png')
        self.x, self.y, self.speed = main_state.player.x, main_state.player.y, RUN_SPEED_PPS
        self.damage = 1

    def get_bb(self):
        return self.x - 4, self.y - 9, self.x + 4, self.y + 9

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        self.y += self.speed

        if self.y > 600:
            game_world.remove_object(self)

    def hit_enemy(self):
        game_world.remove_object(self)




