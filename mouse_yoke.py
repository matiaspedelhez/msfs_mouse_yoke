from pyautogui import size, moveTo
import vgamepad as vg
from pynput import mouse, keyboard
import json

with open("./config.json") as config_file:
    configs = json.load(config_file)

gamepad = vg.VX360Gamepad()
screen_size = size()
maxSteps = configs['throttle_sensitivity']
currentThrottleStep = 0
pixelsToFloatX = 0.0
pixelsToFloatY = 0.0
active = False


def mouseYoke(x, y):
    global pixelsToFloatX
    global pixelsToFloatY

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
        if currentThrottleStep < maxSteps and dy == 1:
            currentThrottleStep += dy
        if currentThrottleStep > 0 and dy == -1:
            currentThrottleStep += dy
        
        stepsToFloat = currentThrottleStep / (maxSteps / 2) - 1

        print(stepsToFloat)
        gamepad.right_joystick_float(x_value_float=stepsToFloat, y_value_float=0)
        gamepad.update()


def onKeyRelease(key):
    global active

    if key == keyboard.KeyCode.from_char(configs["master_key"]):
        active = not active
        if active: moveTo(screen_size.width / 2, screen_size.height / 2)
        print("Yoke is {}!".format("active" if active else "inactive"))
        

if __name__ == "__main__":
    ms = mouse.Listener(
        on_move=mouseYoke,
        on_scroll=throttle)
    kb = keyboard.Listener(
        on_release=onKeyRelease
    )
    ms.start()
    kb.start()
    ms.join()
    kb.join()