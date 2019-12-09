from pico2d import*
import game_framework
import game_world
from bullet import Bullet
import main_state

# PLAYER 42 X 42
padWidth, padHeight = 400,600


PIXEL_PER_METER = (10.0 / 0.5)  # 10 pixel 50 CM
RUN_SPEED_KMPH = 30.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 4

RIGHT_DOWN, RIGHT_UP, LEFT_DOWN, LEFT_UP, SPACE, Key_1, Key_2,  = range(7)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
    (SDL_KEYDOWN, SDLK_SPACE): SPACE,
    (SDL_KEYDOWN, SDLK_1): Key_1,
    (SDL_KEYDOWN, SDLK_2): Key_2
}

class IdleState:

    @staticmethod
    def enter(player, event):
        if event == RIGHT_DOWN:
            player.velocity += RUN_SPEED_PPS
        elif event == LEFT_DOWN:
            player.velocity -= RUN_SPEED_PPS
        elif event == RIGHT_UP:
            player.velocity -= RUN_SPEED_PPS
        elif event == LEFT_UP:
            player.velocity += RUN_SPEED_PPS
        elif event == Key_1:
            if main_state.money >= main_state.upgrade_cost:
                main_state.money -= main_state.upgrade_cost
                main_state.upgrade_cost += 10
                main_state.bullet_damage += 1
        elif event == Key_2:
            if main_state.skill_cooldown <= 0:
                for main_state.enemy in main_state.enemys:
                    main_state.enemy.hp = 0
                player.skill_time = True
                main_state.cooldown_timer = True
                main_state.skill_cooldown = 30


            pass
        player.dir = clamp(-1, player.velocity, 1)

    @staticmethod
    def exit(player, event):
        if event == SPACE:
            player.bullet()

    @staticmethod
    def do(player):
        player.frame = (player.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4

    @staticmethod
    def draw(player):
        player.image.clip_draw(int(player.frame) * 42, 84, 42, 42, player.x, player.y)


class RunState:

    @staticmethod
    def enter(player, event):
        if event == RIGHT_DOWN:
            player.velocity += RUN_SPEED_PPS
        elif event == LEFT_DOWN:
            player.velocity -= RUN_SPEED_PPS
        elif event == RIGHT_UP:
            player.velocity -= RUN_SPEED_PPS
        elif event == LEFT_UP:
            player.velocity += RUN_SPEED_PPS
        elif event == Key_1:
            if main_state.money >= main_state.upgrade_cost:
                main_state.money -= main_state.upgrade_cost
                main_state.upgrade_cost += 10
                main_state.bullet_damage += 1
        elif event == Key_2:
            if main_state.skill_cooldown <= 0:
                for main_state.enemy in main_state.enemys:
                    main_state.enemy.hp = 0
                player.skill_time = True
                main_state.cooldown_timer = True
                main_state.skill_cooldown = 30
        player.dir = clamp(-1, player.velocity, 1)

    @staticmethod
    def exit(player, event):
        if event == SPACE:
            player.bullet()


    @staticmethod
    def do(player):
        player.frame = (player.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4
        player.x += player.velocity * game_framework.frame_time
        player.x = clamp(0, player.x, 400)

    @staticmethod
    def draw(player):
        if player.dir == 1:
            player.image.clip_draw(int(player.frame) * 42, 42, 42, 42, player.x, player.y)
        elif player.dir == -1:
            player.image.clip_draw(int(player.frame) * 42, 0, 42, 42, player.x, player.y)


next_state_table = {
    IdleState: {RIGHT_UP: RunState, LEFT_UP: RunState, RIGHT_DOWN: RunState, LEFT_DOWN: RunState, SPACE: IdleState, Key_1 : IdleState, Key_2 : IdleState},
    RunState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, RIGHT_DOWN: IdleState, LEFT_DOWN: IdleState, SPACE: RunState, Key_1 : RunState, Key_2 : RunState}
}


class Player:
    def __init__(self):
        self.x, self.y = padWidth // 2, 20
        self.image = load_image('./resource/animation01.png')
        self.skill_image = load_image('./resource/explosion2.png')
        self.frame = 0
        self.dir = 0
        self.velocity = 0
        self.skill_time = False
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)

    def get_bb(self):
        return self.x - 21, self.y - 21, self.x + 21, self.y + 21

    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)
        if self.skill_time is True:
            if main_state.skill_time > 0:
                main_state.skill_time -= game_framework.frame_time
                self.skill_image.draw(200,300)
            else:
                self.skill_time = False
                main_state.skill_time = 2

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

    def bullet(self):
        bullets = Bullet(self.x, self.y)
        game_world.add_object(bullets, 1)


