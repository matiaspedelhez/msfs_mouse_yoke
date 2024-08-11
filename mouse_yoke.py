from pyautogui import size, moveTo, getActiveWindow
from pynput import mouse, keyboard
from reprint import output
from threading import Thread
import vgamepad as vg
import logging
import sys
import json
import time


with open("./config.json") as config_file:
    configs = json.load(config_file)


logging.basicConfig(filename=f"./logs/{sys.argv[1]}", format="%(asctime)s - %(message)s")
gamepad = vg.VX360Gamepad()
screen_size = size()

currentThrottleStep = 0
pixelsToFloatX = 0.0
pixelsToFloatY = 0.0
global_x = 0
global_y = 0
active = False

# init the variables to center of the screen
last_x_position = screen_size.width / 2
last_y_position = screen_size.height / 2


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

def isFocused():
    title = getActiveWindow().title
    width = getActiveWindow().width
    height = getActiveWindow().height
    
    # Checking if the game is focused or not and if it's in fullscreen
    if "Microsoft Flight Simulator" in title and width == screen_size.width and height == screen_size.height:
        return True
    else:
        return False

def onKeyRelease(key):
    global active
    global last_x_position
    global last_y_position

    # Only executed when the game is focused
    if key == keyboard.KeyCode.from_char(configs["master_key"]) and isFocused():
        if active:
            # getting deactivated
            last_x_position = global_x
            last_y_position = global_y

        active = not active

        if configs["remember_last_position"]:
            # return to last position
            if active: moveTo(last_x_position, last_y_position)
            mouseYoke(last_x_position, last_y_position)
            
        if not configs["remember_last_position"]:
            # return to center
            if active: moveTo(screen_size.width / 2, screen_size.height / 2)
            mouseYoke(screen_size.width / 2, screen_size.height / 2)

    
    if key == keyboard.KeyCode.from_char(configs["center_xy_axes_key"]) and isFocused():
        moveTo(screen_size.width / 2, screen_size.height / 2)

        if active:
            mouseYoke(screen_size.width / 2, screen_size.height / 2)
        

def userInterface():
    with output(initial_len=8, interval=0) as output_lines:
        while True:

            output_lines[0] = f"+{' Status: ' + ('ACTIVE' if active else 'INACTIVE') + ' ':—^60}+"
            output_lines[1] = f"|{'':^60}|"
            output_lines[2] = f"|{'Axis':^20}{'Raw input':^20}{'Conversion':^20}|"
            output_lines[3] = f"+{'':—^60}+"
            output_lines[4] = f"|{'X':^20}{global_x:^20}{'{:.2f}'.format((pixelsToFloatX + 1) * 50) + '%':^20}|"
            output_lines[5] = f"|{'Y':^20}{global_y:^20}{'{:.2f}'.format((pixelsToFloatY + 1) * 50) + '%':^20}|"
            output_lines[6] = f"|{'THROTTLE':^20}{currentThrottleStep:^20}{'{:.2f}'.format((currentThrottleStep * 100 / configs['throttle_sensitivity'])) + '%':^20}|"
            output_lines[7] = f"+{'':—^60}+"

            time.sleep(0.05)


if __name__ == "__main__":
    logging.warning("mouse_yoke.py is now running\n\n")

    try:
        ui = Thread(target=userInterface)
        ms = mouse.Listener(on_move=mouseYoke, on_scroll=throttle)
        kb = keyboard.Listener(on_release=onKeyRelease)
        
        ms.start()
        kb.start()
        ui.start()
        ms.join()
        kb.join()

    except Exception as e:
        logging.critical("Exception occurred", exc_info=True)