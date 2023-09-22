from microbit import *

def main():
    x = 2
    y = 2

    display.set_pixel(x, y, 9)

    while True:
        print("x: ", accelerometer.get_x())
        print("y: ", accelerometer.get_y())

        accel_x = accelerometer.get_x()
        accel_y = accelerometer.get_y()

        display.set_pixel(x, y, 0)

        if accel_y < -100 and y > 0:
            y = y - 1
        elif accel_y > 100 and y < 4:
            y = y + 1
        elif accel_x < -100 and x > 0:
            x = x - 1
        elif accel_x > 100 and x < 4:
            x = x + 1

        display.set_pixel(x, y, 9)

        sleep(1000)

main()
