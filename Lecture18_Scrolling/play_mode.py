import random
import json
import os

from pico2d import *
import game_framework
import game_world
from ball import Ball
import server
from boy import Boy

# fill here
from background import FixedBackground as Background



def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            server.boy.handle_event(event)



def init():
    server.background = Background()
    game_world.add_object(server.background, 0)
    server.boy = Boy()
    game_world.add_object(server.boy, 1)
    server.balls = []  # 공 리스트 생성
    for _ in range(100):  # 100번 반복
        ball = Ball()  # 공 생성
        server.balls.append(ball)  # 공 리스트에 추가
        game_world.add_object(ball, 1)  # 게임 월드에 추가  # 게임 월드에 공 추가
def finish():
    game_world.clear()
    pass


def update():
    game_world.update()
    game_world.handle_collisions()

def draw():
    clear_canvas()
    game_world.render()
    update_canvas()

def pause():
    pass

def resume():
    pass



