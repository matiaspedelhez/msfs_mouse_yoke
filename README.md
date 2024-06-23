# msfs_mouse_yoke

Warning: This project is no longer being maintained.

This is a small script written in Python that lets you fly with your mouse in Microsoft Flight Simulator 2020. (Why is this not implemented in the game yet?).


## How does it work?

The script is always listening for the mouse position and it transforms that into an xbox controller input. It also listens for the scroll wheel position, that way, you can use it as a throttle. 


## Installation

1. Download and install [Python](https://www.python.org/).
	  > Make sure to add Python to the Path during the installation **(important!)**
   
   ![add_python_to_path](https://github.com/matiaspedelhez/msfs_mouse_yoke/assets/81604853/5c6e7547-89cb-4376-98ce-2f2ca9b64d85)

	
 2. Download the latest version of the script from the [releases section](https://github.com/matiaspedelhez/msfs_mouse_yoke/releases).
 3. Configure the script as you like! 
	 > You can modify the text file 'config.json'

```javascript
// config.json

{ 
    "master_key": ",",
    "throttle_sensitivity": 20,
    "remember_last_position": true,
    "center_xy_axes_key": "."
}

```

## Usage

 1. Open the file **run.bat**. If its the first time you are opening it, it will install some dependencies that are required.
 2. To activate the script, press the **master_key**. Default key is comma ",".
    
![inactive_state](https://github.com/matiaspedelhez/msfs_mouse_yoke/assets/81604853/32de6ea2-68ab-4f7d-a63a-92237358baf7)

## Settings in detail

1. "master_key": "," | The key for turning on/off the script.
2. "throttle_sensitivity": 20 | How many scroll-wheel steps are required to go from 0% to 100% throttle.
3. "remember_last_position": true | If true, the position of the yoke will be remembered when you switch on/off the script.
4. "center_xy_axes_key": "." | The key for centering the yoke axes.


## Keep in mind that...
- When you are setting up the bindings in the game, I recommend removing ALL bindings that are set by default for xbox controllers, and leaving only the axis that you need (which are only two).\
![image](https://user-images.githubusercontent.com/81604853/198916272-5f92a8c7-013a-4614-98bd-637830455754.png)

- Clear all the "filters" that the game adds to the xbox controller. Leave it as raw as you can.\
![image](https://user-images.githubusercontent.com/81604853/198917548-432d4f79-d778-429b-b1d3-c74b97eac5b7.png)


Happy flying!
