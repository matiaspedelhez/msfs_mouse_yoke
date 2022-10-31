import pyautogui as pygui
import vgamepad as vg
import keyboard
import time
import json
import os

with open("./config.json") as config_file:
    configs = json.load(config_file)

gamepad = vg.VX360Gamepad()
screen_size = pygui.size()


def mouseYoke():
    active = True
    pygui.moveTo(screen_size.width / 2, screen_size.height / 2)

    os.system('cls')
    print(" ## Mouse Yoke init ##\nPress '{}' to turn on and off the script.".format(configs["master_key"]))

    while True:
        [x, y] = pygui.position()

        if active:
            pixelsToFloatX = x / (screen_size.width / 2) - 1
            pixelsToFloatY = y / (screen_size.height / 2) - 1

            gamepad.left_joystick_float(x_value_float=pixelsToFloatX, y_value_float=pixelsToFloatY)
            gamepad.update()

        if(keyboard.is_pressed(configs["master_key"])):
            active = not active

            os.system('cls')
            print("Mouse Yoke is now {}! Switch using key/hotkey '{}'".format("active" if active else "inactive", configs["master_key"]))
            
            time.sleep(0.1)

        time.sleep(0.001) # for performance issues


if __name__ == "__main__":
    mouseYoke()
