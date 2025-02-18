from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

def draw_character(x,y):
    clear_canvas_now()
    character.draw_now(x,y)
    delay(0.01)

def run_top():
    print('top')
    for x in range(0,800,10):
        draw_character(x,550)
    
    pass

def run_right():
    print('right')
    for y in range(600,0,-10):
        draw_character(800,y)
    pass

def run_bottom():
    print('bottom')
    for x in range(800,0,-10):
        draw_character(x,0)
    pass

def run_left():
    print('left')
    for y in range(0,600,10):
        draw_character(0,y)
    pass

def run_rectangle():
    print('rectangle')
    run_top()
    run_right()
    run_bottom()
    run_left()
    
    pass

def run_circle():
    print('circle')

    r, cx, cy = 300, 800//2, 600//2
    
    for d in range(0,360):
        x = r * math.cos(math.radians(d)) + cx
        y = r * math.sin(math.radians(d)) + cy
        
        draw_character(x,y)

def run_left_diagonal():
    print('left_diagonal')
    x, y = 0, 0
    while x < 400:
        draw_character(x,y)
        x += 2
        y += 2

def run_right_diagonal():
    print('right_diagonal')
    x, y = 400, 400
    while x < 800:
        draw_character(x,y)
        x += 2
        y -= 2

def run_triangle():
    print('triangle')
    run_bottom()
    run_left_diagonal()
    run_right_diagonal()
    pass

while True:
    run_circle()
    run_rectangle()
    run_triangle()

close_canvas()
