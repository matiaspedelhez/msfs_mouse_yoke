from MouseController import MouseController
import vgamepad as vg
import sys
import time
import logging
import threading
import json

FORMAT = '%(asctime)s:PY::%(lineno)d:%(levelname)s - %(message)s'
logging.basicConfig(level=logging.DEBUG, encoding='utf-8', filename=f"./logs/{sys.argv[1]}.log", format=FORMAT)
log = logging.getLogger(__name__)

def listenForCommands(mouse_controller):
    # listen for commands from Nodejs by listening to std
    command = ""
    commands = ["RUN", "PAUSE", "FORCE_STOP", "SET_MASTER_KEY", "SET_THROTTLE_SENSITIVITY"]
    
    while True:
        time.sleep(0.1)
        try:
            for line in sys.stdin:
                if line.endswith("\n"):
                    command = line.removesuffix("\n")
                    break

            if command is not False: command = eval(command)
        except Exception as err:
            log.critical(err)
        
        if command["action"] in commands:
            log.info("Request received: %s", command["action"])

            match command["action"]:
                case "RUN":
                    mouse_controller.run()
                case "PAUSE":
                    mouse_controller.pause()
                case "FORCE_STOP":
                    mouse_controller.forceStop()
                case "SET_MASTER_KEY":
                    pass
                case "SET_THROTTLE_SENSITIVITY":
                    if command["input"].isnumeric():
                        mouse_controller.wheel_sensitivity = int(command["input"])

def sendStatus():
    # send commands to std by printing them - later grabbed by Nodejs
    while True:
        time.sleep(0.1)
        
        print(json.dumps([{
                "type": "mouse_controller_data",
                "data": {
                    "raw_x": mouse_controller.raw_position_x,
                    "raw_y": mouse_controller.raw_position_y,
                    "raw_wheel": mouse_controller.raw_scroll_position,
                    "mc_status": mouse_controller.status,
                    "transformed_x": mouse_controller.transformed_position_x,
                    "transformed_y": mouse_controller.transformed_position_y,
                    "transformed_wheel": mouse_controller.transformed_scrollwheel
                }
            }], separators=(',', ':')),
            end="",
            flush=True,
        )
        sys.stdout.flush()

if __name__ == "__main__":
    # script init
    mouse_controller = MouseController(gamepad=vg.VX360Gamepad())
    mouse_controller.run()

    # communicate back and forth with Node.js
    threading.Thread(target=lambda: listenForCommands(mouse_controller)).start()
    threading.Thread(target=sendStatus).start()