from pico2d import *
import game_world
import main_state


PIXEL_PER_METER = (10.0 / 0.5)  # 10 pixel 50 cm
RUN_SPEED_KMPH = 0.1  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)


class Bullet:
    image = None

    def __init__(self, x=200, y=30):
        if Bullet.image is None:
            Bullet.image = load_image('./resource/bullet.png')
        self.x, self.y = x, y
        self.speed = RUN_SPEED_PPS
        self.damage = main_state.bullet_damage

    def update(self):
        self.y += self.speed

        if self.y > 600:
            game_world.remove_object(self)

        for main_state.enemy in main_state.enemys:
            if main_state.collide(self, main_state.enemy):
                main_state.enemy.hp -= self.damage
                game_world.remove_object(self)

    def draw(self):
        self.image.draw(self.x, self.y)

    def get_bb(self):
        return self.x - 4, self.y - 9, self.x + 4, self.y + 9




