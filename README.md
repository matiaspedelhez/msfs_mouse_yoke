# msfs_mouse_yoke

This is a small script written in Python that lets you fly with your mouse in Microsoft Flight Simulator 2020. (Why is this not implemented in the game yet?).


## How does it work?

The script is always listening for the mouse position, and it transforms that into an xbox controller input. That way you can bind it in the game. 


## Installation

To run the script, just open the file run.bat. You must have Python installed in your computer.\
If you want to modify the key for turning the script on/off, you can edit config.json:

```javascript
// config.json

{
  "master_key": ","
}

```

The default key is comma. You can also use hotkeys, i.e. "shift+s" or "ctrl+shift+=".

This script doesn't require any external software like vJoy or Virtual Controller.

#### Keep in mind that...
- When you are setting up the bindings in the game, I recommend removing ALL bindings that are set by default for xbox controllers, and leaving only the axis that you need (which are only two).\
![image](https://user-images.githubusercontent.com/81604853/198916272-5f92a8c7-013a-4614-98bd-637830455754.png)

- Clear all the "filters" that the game adds to the xbox controller. Leave it as raw as you can.\
![image](https://user-images.githubusercontent.com/81604853/198917548-432d4f79-d778-429b-b1d3-c74b97eac5b7.png)

#### Side note: I made this script in a few minutes, so its not perfect by any means. It probably has some bugs and its not that usable because you don't have a way to control the throttle (critical) nor the rudder (not that critical). I will add those soon.


Happy flying!
