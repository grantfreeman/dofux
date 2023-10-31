from enum import Enum
from pynput.mouse import Button, Controller
from typing import Tuple
from time import sleep

DELAY = 0.100
LIGHT_X = 924

def slot_pixel(slot: int) -> Tuple:
    SLOT_X = [600, 655, 710, 765, 820]
    SLOT_Y = 650
    return (SLOT_X[slot - 1], SLOT_Y)

def hue_pixel(value: int) -> int:
    # convert from 0-360 to 0-386
    HUE_MIN_X = 517
    HUE_MAX_X = 902
    HUE_RANGE = HUE_MAX_X - HUE_MIN_X
    base = (value * HUE_RANGE) / 360
    return base + HUE_MIN_X

def sat_pixel(value: int) -> int:
    # convert from 0-100% to 0-149
    SAT_MIN_Y = 674
    SAT_MAX_Y = 823
    SAT_RANGE = SAT_MAX_Y - SAT_MIN_Y
    base = (value * SAT_RANGE) / 100
    return SAT_MAX_Y - base

def light_pixel(value: int) -> int:
    # convert from 0-100% to 0-149
    LIGHT_MIN_Y = 674
    LIGHT_MAX_Y = 823
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
    user = mouse.position
    color_hsl(1, 24, 40, 52)
    color_hsl(2, 180, 30, 10)
    color_hsl(3, 170, 36, 24)
    color_hsl(4, 40, 80, 50)
    color_hsl(5, 10, 32, 28)
    mouse.position = user