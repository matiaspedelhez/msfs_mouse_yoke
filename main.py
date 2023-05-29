from MouseController import MouseController
from gui import app
import vgamepad as vg
import tkinter, customtkinter
import time

scrollLabel = customtkinter.CTkProgressBar(app, width=400, height=20, fg_color="white", progress_color="blue")
scrollLabel.pack(padx=10, pady=10)
mouse_controller = MouseController(gamepad=vg.VX360Gamepad())
mouse_controller.run()

def doSomething():
    scrollLabel.set(mouse_controller.raw_scroll_position / 20)

mouse_controller.onUpdate(doSomething)







app.mainloop()

while True:
    scrollLabel.set(mouse_controller.transformed_scrollwheel / 20)
    print('hi')
    time.sleep(0.05)
    