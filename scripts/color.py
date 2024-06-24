from enum import Enum
from pynput.mouse import Button, Controller
from typing import Tuple
from time import sleep

DELAY = 0.100
LIGHT_X = 929

def slot_pixel(slot: int) -> Tuple:
    SLOT_X = [620, 675, 730, 785, 840]
    SLOT_Y = 655
    return (SLOT_X[slot - 1], SLOT_Y)

def hue_pixel(value: int) -> int:
    # convert from 0-360 to 0-386
    HUE_MIN_X = 523
    HUE_MAX_X = 908
    HUE_RANGE = HUE_MAX_X - HUE_MIN_X
    base = (value * HUE_RANGE) / 360
    return base + HUE_MIN_X

def sat_pixel(value: int) -> int:
    # convert from 0-100% to 0-149
    SAT_MIN_Y = 679
    SAT_MAX_Y = 828
    SAT_RANGE = SAT_MAX_Y - SAT_MIN_Y
    base = (value / 100) * SAT_RANGE
    return SAT_MAX_Y - base

def light_pixel(value: int) -> int:
    # convert from 0-100% to 0-149
    LIGHT_MIN_Y = 679
    LIGHT_MAX_Y = 828
    LIGHT_RANGE = LIGHT_MAX_Y - LIGHT_MIN_Y
    base = (value * LIGHT_RANGE) / 100
    return LIGHT_MAX_Y - base

def color_hsl(slot: int, hue: int, saturation: int, lightness: int):
    # select slot
    mouse.position = slot_pixel(slot)
    mouse.click(Button.left, 1)
    sleep(DELAY)
    print(f'SLOT {slot} :', mouse.position)

    # select hue and saturation
    mouse.position = (hue_pixel(hue), sat_pixel(saturation))
    mouse.click(Button.left, 1)
    sleep(DELAY)
    print('HUE & SAT :', mouse.position)

    # select lightness
    mouse.position = (LIGHT_X, light_pixel(lightness))
    mouse.click(Button.left, 1)
    sleep(DELAY)
    print('LIGHT :', mouse.position)

    # pad output
    print()

if __name__ == "__main__":
    mouse = Controller()

    # save for later
    user = mouse.position

    # enutrof
    color_hsl(1, 24, 52, 50)
    color_hsl(2, 40, 50, 70)
    color_hsl(3, 140, 32, 24)
    color_hsl(4, 38, 80, 50)
    color_hsl(5, 10, 32, 28)

    # revert to original mouse position
    mouse.position = user