from pyautogui import size, moveTo
from pynput import mouse, keyboard
from threading import Thread
import logging
import sys
import json
import time


# logging.basicConfig(filename=f"./logs/{sys.argv[1]}", format="%(asctime)s - %(message)s")

class MouseController:
    def __init__(self, gamepad, status="Stopped"):
        self.status = "Stopped" # "Stopped" or "Paused" or "Running"
        self.gamepad = gamepad
        self.raw_position_x = None
        self.raw_position_y = None
        self.transformed_position_x = 0
        self.transformed_position_y = 0
        self.transformed_scrollwheel = 0
        self.screen_size = {"width": None, "height": None}
        self.mouse_instance = None
        self.keyboard_instance = None
        

    def __loop(self, mouseInput, keysInput):
        # creating instance of pynput
        movement, scroll = mouseInput
        
        self.mouse_instance = mouse.Listener(on_move=movement, on_scroll=scroll)
        self.keyboard_instance = keyboard.Listener(on_release=keysInput)
    
        self.mouse_instance.start()
        self.keyboard_instance.start()

    def __stopLoop(self):
        # deleting instance of pynput
        del self.mouse_instance
        del self.keyboard_instance

    def __mouseMovementCallback(self):
        if self.status == "Running":
            self.__transformRawPositions()

            self.gamepad.left_joystick_float(x_value_float=self.transformed_position_x, y_value_float=self.transformed_position_y)
            self.gamepad.update()

    def __scrollwheelCallback(self):
        pass

    def __getScreenSize(self):
        # get width and height of screen (includes multiple monitors)
        self.screen_size["width"], self.screen_size["height"] = size()

    def __transformRawPositions(self, scrollSensitivity, dy):
        # transform pointer cordinates into -1 to 1 floatable values 
        self.__getScreenSize()

        # transform mouse value
        if self.raw_position_x >= 0 and self.raw_position_x  <= self.screen_size.width:
            self.transformed_position_x = self.raw_position_x / (self.screen_size.width / 2) - 1
        if self.raw_position_y >= 0 and self.raw_position_y <= self.screen_size.height:
            self.transformed_position_y = self.raw_position_y / (self.screen_size.height / 2) - 1
        
        # transform scrollwheel value
        if self.transformed_scrollwheel < scrollSensitivity and dy == 1:
            self.transformed_scrollwheel += dy
        if self.transformed_scrollwheel > 0 and dy == -1:
            self.transformed_scrollwheel -= dy


    def run(self, screen_size_x, screen_size_y):
        if self.status == "Running":
            logging.warning("Cannot start MouseController: it is already running.")
            return
        else:
            self.status = "Running"
            logging.info("MouseController is now running.")


    def stop(self):
        if self.status == "Stopped":
            logging.warning("Cannot stop MouseController: it is already stopped.")
            return
        else:
            self.status = "Stopped"
            logging.info("MouseController is now stopped.")


    def pause(self):
        if self.status == "Paused":
            logging.warning("Cannot pause MouseController: it is already paused.")
            return
        else:
            self.status = "Paused"
            logging.info("MouseController is now paused.")    

mouse_controller = MouseController #debug
mouse_controller.run(1920, 1080) #debug