from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

def run_rectangle():
    print('rectangle')
    pass

def run_circle():
    print('circle')

    r, cx, cy = 300, 800//2, 600//2
    
    for d in range(0,360):
        x = r * math.cos(math.radians(d)) + cx
        y = r * math.sin(math.radians(d)) + cy
        
        clear_canvas_now()
        character.draw_now(x,y)
        delay(0.01)
        pass


while True:
    run_circle()
    run_rectangle()
    break

close_canvas()
