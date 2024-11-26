from pico2d import *
import game_world
import game_framework
import random
import server


class Ball:
    def __init__(self, x=None, y=None):
        self.image = load_image('ball21x21.png')  # 공 이미지
        self.x = x if x is not None else random.randint(0, server.background.w)  # 월드 좌표 기준 x
        self.y = y if y is not None else random.randint(0, server.background.h)  # 월드 좌표 기준 y

    def update(self):
        # 소년과의 충돌을 확인
        if self.check_collision(server.boy):
            game_world.remove_object(self)  # 충돌 시 공을 게임 월드에서 삭제
            server.balls.remove(self)  # 리스트에서 공을 삭제

    def check_collision(self, boy):
        ball_bb = self.get_bb()
        boy_bb = boy.get_bb()

        # AABB 충돌 감지
        return ball_bb[0] < boy_bb[2] and ball_bb[2] > boy_bb[0] and ball_bb[1] < boy_bb[3] and ball_bb[3] > boy_bb[1]

    def draw(self):
        # Viewport 좌표로 변환 (월드 좌표에서 Viewport 위치 빼기)
        screen_x = self.x - server.background.window_left
        screen_y = self.y - server.background.window_bottom
        self.image.draw(screen_x, screen_y)

    def get_bb(self):
        # Bounding Box도 월드 좌표 기준으로 유지
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10
