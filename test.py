from pyautogui import size, moveTo
from pynput import mouse, keyboard
from reprint import output
from threading import Thread
import vgamepad as vg
import logging
import sys
import json
import time


logging.basicConfig(filename=f"./logs/{sys.argv[1]}", format="%(asctime)s - %(message)s")
gamepad = vg.VX360Gamepad()
screen_size = size()

currentThrottleStep = 0
pixelsToFloatX = 0.0
pixelsToFloatY = 0.0
global_x = 0
global_y = 0
active = False

def mouseYoke(x, y):
    global pixelsToFloatX, pixelsToFloatY
    global global_x, global_y

    global_x = x
    global_y = y
    
    if active:
        if x >= 0 and x <= screen_size.width:
            pixelsToFloatX = x / (screen_size.width / 2) - 1
        if y >= 0 and y <= screen_size.height:
            pixelsToFloatY = y / (screen_size.height / 2) - 1

        gamepad.left_joystick_float(x_value_float=pixelsToFloatX, y_value_float=pixelsToFloatY)
        gamepad.update()


def throttle(x, y, dx, dy):
    global currentThrottleStep
     
    if active:
        if currentThrottleStep < configs['throttle_sensitivity'] and dy == 1:
            currentThrottleStep += dy
        if currentThrottleStep > 0 and dy == -1:
            currentThrottleStep += dy
        
        stepsToFloat = currentThrottleStep / (configs['throttle_sensitivity'] / 2) - 1

        gamepad.right_joystick_float(x_value_float=stepsToFloat, y_value_float=0)
        gamepad.update()


def onKeyRelease(key):
    global active

    if key == keyboard.KeyCode.from_char(configs["master_key"]):
        active = not active
        if active: moveTo(screen_size.width / 2, screen_size.height / 2)


# if __name__ == "__main__":
    
#     with open("./config.json") as config_file:
#     configs = json.load(config_file)
#     logging.warning("mouse_yoke.py is now running\n\n")

#     try:
#         ms = mouse.Listener(on_move=mouseYoke, on_scroll=throttle)
#         kb = keyboard.Listener(on_release=onKeyRelease)
        
#         ms.start()
#         kb.start()
#         ui.start()
#         ms.join()
#         kb.join()

#     except Exception as e:
#         logging.critical("Exception occurred", exc_info=True)