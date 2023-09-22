from microbit import *
from random import randrange

EMPTY = 0
SNAKE = 2
APPLE = 4

game_board = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 2, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

NORTH = 0
SOUTH = 1
EAST = 2
WEST = 3

# map to be the same as the led matrix
def get_board_state(x, y):
    return game_board[y][x]

def set_board_state(x, y, value):
    game_board[y][x] = value

def move(snake, x, y):
    # (tail_x, tail_y) = snake[-1]
    tail_x = snake[-1][0]
    tail_y = snake[-1][1]

    print("--- move")
    print("head: (", x, ", ", y, ")")
    print("tail: (", tail_x, ", ", tail_y, ")")

    set_board_state(tail_x, tail_y, EMPTY)
    snake = snake[:-1]
    set_board_state(x, y, SNAKE)
    snake.insert(0, [x, y])

    return snake

def new_apple():
    while True:
        apple_x = randrange(5)
        apple_y = randrange(5)

        if get_board_state(apple_x, apple_y) == EMPTY:
            set_board_state(apple_x, apple_y, APPLE)
            break

def reset():
    for i in range(5):
        for j in range(5):
            set_board_state(i, j, EMPTY)

    set_board_state(2, 2, SNAKE)
    new_apple()
    return [[2, 2]]

def main():
    x = 2
    y = 2
    prev_x = 2
    prev_y = 2
    direction = NORTH

    x_direction = EAST
    y_direction = NORTH

    snake = [[x, y]]

    new_apple()

    while True:
        print("x: ", accelerometer.get_x())
        print("y: ", accelerometer.get_y())

        accel_x = accelerometer.get_x()
        accel_y = accelerometer.get_y()

        prev_x = x
        prev_y = y

        if accel_y < -100 and y > 0:
            y = y - 1
            y_direction = NORTH
        elif accel_y > 100 and y < 4:
            y = y + 1
            y_direction = SOUTH
        elif accel_x < -100 and x > 0:
            x = x - 1
            x_direction = EAST
        elif accel_x > 100 and x < 4:
            x = x + 1
            x_direction = WEST

        if prev_x != x or prev_y != y:
            if get_board_state(x, y) == APPLE:
                set_board_state(x, y, SNAKE)
                snake.insert(0, [x, y])
                new_apple()
            elif get_board_state(x, y) == EMPTY:
                snake = move(snake, x, y)
            elif get_board_state(x, y) == SNAKE:
                display.show(Image.SKULL)
                sleep(3000)
                snake = reset()
                x = 2
                y = 2
                prev_x = 2
                prev_y = 2

        for i in range(5):
            for j in range(5):
                b_state = get_board_state(i, j)
                if b_state == SNAKE:
                    display.set_pixel(i, j, 4)
                elif b_state == APPLE:
                    display.set_pixel(i, j, 7)
                else:
                    display.set_pixel(i, j, 0)

        sleep(1000)

main()
