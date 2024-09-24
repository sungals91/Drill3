from pico2d import *

def run_rectangle():
    print('rectangle')
    pass

def run_circle():
    print('circle')
    pass

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

while True:
    run_circle()
    run_rectangle()

close_canvas()
