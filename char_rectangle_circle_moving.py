from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

def run_rectangle():
    print('rectangle')
    pass

def run_circle():
    clear_canvas_now()
    character.draw_now(400,300)
    delay(1)
    pass


while True:
    run_circle()
    run_rectangle()
    break

close_canvas()
