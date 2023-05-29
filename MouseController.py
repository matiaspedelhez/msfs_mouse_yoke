from pyautogui import size, moveTo
from pynput import mouse, keyboard
import vgamepad as vg
import logging

# logging.basicConfig(filename=f"./logs/{sys.argv[1]}", format="%(asctime)s - %(message)s")

class MouseController:
    def __init__(self, gamepad, status="Paused"):
        self.status = status # "Paused" or "Running"
        self.gamepad = gamepad
        self.raw_position_x = 0
        self.raw_position_y = 0
        self.raw_scroll_position = 0
        self.transformed_position_x = 0
        self.transformed_position_y = 0
        self.transformed_scrollwheel = 0
        self.screen_size = {"width": 0, "height": 0}
        self.mouse_instance = None
        self.keyboard_instance = None
        self.__on_update_callback = None

        self.__loop(self.__mouseMovementCallback, self.__scrollwheelCallback)
        self.__getScreenSize()

    
    def __loop(self, on_move, on_scroll):
        # creating and starting pynput listeners for mouse and keyboard
        self.mouse_instance = mouse.Listener(on_move=on_move, on_scroll=on_scroll)
        # self.keyboard_instance = keyboard.Listener(on_release=on_release)
    
        self.mouse_instance.start()
        # self.keyboard_instance.start()

    def __mouseMovementCallback(self, x, y):
        self.raw_position_x = x
        self.raw_position_y = y
        self.__transformRawPositions()

        if self.status == "Running":
            self.gamepad.left_joystick_float(x_value_float=self.transformed_position_x, y_value_float=self.transformed_position_y)
            self.gamepad.update()
            try:
                self.__on_update_callback()
            except:
                pass
    def __scrollwheelCallback(self, x, y, dx, dy):
        self.__transformRawScroll(20, dy)

        if self.status == "Running":
            self.gamepad.right_joystick_float(x_value_float=self.transformed_scrollwheel, y_value_float=0)
            self.gamepad.update()
            try:
                self.__on_update_callback()
            except:
                pass

    def __getScreenSize(self):
        # get width and height of screen (includes multiple monitors)
        self.screen_size["width"], self.screen_size["height"] = size()
        logging.info(self.screen_size)

    def __transformRawPositions(self):
        # transform mouse pointer coordinates into -1 to 1 floatable values 
        if self.raw_position_x >= 0 and self.raw_position_x  <= self.screen_size['width']:
            self.transformed_position_x = self.raw_position_x / (self.screen_size['width'] / 2) - 1
        if self.raw_position_y >= 0 and self.raw_position_y <= self.screen_size['height']:
            self.transformed_position_y = self.raw_position_y / (self.screen_size['height'] / 2) - 1

    def __transformRawScroll(self, sensitivity, dy):
        # transform scrollwheel value into -1 to 1 floatable values 
        if self.raw_scroll_position < sensitivity and dy == 1:
            self.raw_scroll_position += dy
        if self.raw_scroll_position > 0 and dy == -1:
            self.raw_scroll_position += dy

        self.transformed_scrollwheel = self.raw_scroll_position / (sensitivity / 2) - 1

    def run(self):
        if self.status == "Running":
            logging.warning("Cannot start MouseController: it is already running.")
            return
        
        self.status = "Running"
        try:
            self.__on_update_callback()
        except:
            pass
        logging.info("MouseController is now running.")

    def pause(self):
        if self.status == "Paused":
            logging.warning("Cannot pause MouseController: it is already paused.")
            return
        else:
            self.status = "Paused"
            try:
                self.__on_update_callback()
            except:
                pass
            logging.info("MouseController is now paused.")   

    def onUpdate(self, on_update_callback):
        self.__on_update_callback = on_update_callback

    def forceStop(self):
        # deleting instance of pynput
        del self.mouse_instance
        del self.keyboard_instance 
        logging.warning("Force stopping mouse and keyboard listeners.")

        self.status = "Stopped"
        try:
            self.__on_update_callback()
        except:
            pass