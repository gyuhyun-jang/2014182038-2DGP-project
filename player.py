from pico2d import*

padWidth,padHeight = 480,640

RIGHT_DOWN,LEFT_DOWN,RIGHT_UP,LEFT_UP,SPACE_DOWN,SPACE_UP = range(6)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
    (SDL_KEYDOWN, SDLK_SPACE) : SPACE_DOWN,
    (SDL_KEYUP, SDLK_SPACE) : SPACE_UP
}



class Player:
    def __init__(self):
        self.x, self.y = padWidth // 2, 20
        self.frame = 0
        self.dir = 0
        self.image = load_image('animation01.png')

    def update(self):
        self.frame = (self.frame + 1) % 4
        self.x += self.dir * 5
        self.x = clamp(0,self.x,480)
        if self.dir < 0:
            self.state = 0
        elif self.dir > 0:
            self.state = 1
        elif self.dir == 0:
            self.state = 2

    def draw(self):
        self.image.clip_draw(self.frame*42, 42 * self.state, 42, 42, self.x, self.y)
