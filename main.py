from MouseController import MouseController
from gui import app
import vgamepad as vg
import tkinter, customtkinter
import time

scrollLabel = customtkinter.CTkProgressBar(app, width=400, height=20)
mouseXLabel = customtkinter.CTkProgressBar(app, width=400, height=20)
mouseYLabel = customtkinter.CTkProgressBar(app, width=400, height=20)

scrollLabel.pack(padx=10, pady=10)
mouseXLabel.pack(padx=10, pady=10)
mouseYLabel.pack(padx=10, pady=10)

statusLabel = customtkinter.CTkLabel(app)
statusLabel.pack()

mouse_controller = MouseController(gamepad=vg.VX360Gamepad())
mouse_controller.run()

stopButton = customtkinter.CTkButton(app, text="Stop", command=mouse_controller.pause)
stopButton.pack()

runButton = customtkinter.CTkButton(app, text="Run", command=mouse_controller.run)
runButton.pack()

def onUpdate():
    time.sleep(0.05)
    scrollLabel.set(mouse_controller.transformed_scrollwheel / 2)
    mouseXLabel.set(mouse_controller.transformed_position_x / 2)
    mouseYLabel.set(mouse_controller.transformed_position_y / 2)
    statusLabel.text(mouse_controller.status)


mouse_controller.onUpdate(onUpdate)







app.mainloop()

while True:
    scrollLabel.set(mouse_controller.transformed_scrollwheel / 20)
    print('hi')
    time.sleep(0.05)
    