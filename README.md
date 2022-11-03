# msfs_mouse_yoke

This is a small script written in Python that lets you fly with your mouse in Microsoft Flight Simulator 2020. (Why is this not implemented in the game yet?).


## How does it work?

The script is always listening for the mouse position and it transforms that into an xbox controller input. It also listens for the scroll wheel position, that way, you can use it as a throttle. 


## Installation

To run the script, just open the file run.bat. You must have Python installed in your computer.\\
You can modify `"master_key"` key for turning on or off the script. Currently, it doesn't support key combinations such as shift+s.\

```javascript
// config.json

{
  "master_key": ",",
  "throttle_sensitivity": 20
}

```

You will also find `"throttle_sensitivity"`. It lets you set how many steps your throttle would have. Default value is 20, so each step would equal to 5% of thrust.

Note: This script doesn't require any external software like vJoy or Virtual Controller.

#### Keep in mind that...
- When you are setting up the bindings in the game, I recommend removing ALL bindings that are set by default for xbox controllers, and leaving only the axis that you need (which are only two).\
![image](https://user-images.githubusercontent.com/81604853/198916272-5f92a8c7-013a-4614-98bd-637830455754.png)

- Clear all the "filters" that the game adds to the xbox controller. Leave it as raw as you can.\
![image](https://user-images.githubusercontent.com/81604853/198917548-432d4f79-d778-429b-b1d3-c74b97eac5b7.png)


Happy flying!