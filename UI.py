from pico2d import*
import game_world
import game_framework
import main_state

font = None

class UI_Manager:
    def __init__(self):
        self.font = load_font('./resource/ENCR10B.TTF', 12)

    def update(self):
        pass

    def enter(self):
        pass

    def exit(self):
        pass

    def draw(self):
        self.font.draw(300, 560, 'Time : %3.2f' % (main_state.time), (0, 0, 0))
        self.font.draw(300, 500,'Damage : %d' % (main_state.bullet_damage), (0, 0, 0))
        self.font.draw(300, 540,'Kill : %d' % (main_state.kill_score), (0, 0, 0))
        self.font.draw(300, 520, 'Life : %d' % (main_state.player_life), (0, 0, 0))
        self.font.draw(300, 460, 'Upgrade cost : %d' %(main_state.upgrade_cost), (0, 0, 0))
        self.font.draw(300, 480, 'Money : %d' %(main_state.money), (0,0,0))