# xfce4-x11-movecursor-active-window
I made this script because I wanted to move my cursor to the active window when I alt tabbed

## Scripts
### Bash script
This a simple script you can keybind, it will move the cursor to the center of the current active window.
### AutoKey python script
XFCE4 by default doesn't allow conflicting keyboard shorcuts for different actions.
This script is meant to be used with AutoKey.

It will send the ALT + TAB for you so you can set the script to be run with ALT + TAB. And it will wait for you to release alt before executing the rest of the script.

So for that to work correctly you need to fill the KEYBOARD_ID and ALT_KEYCODE variables with the correct xinput values as described on the script.

For ej on my keyboard and keyboard layout KEYBOARD_ID is 9 and ALT_KEYCODE is 64

### xmffw alternative
An alternative version of the AutoKey script but it uses [XMouseFollowFocusedWindow](https://github.com/Vasil-Todorov/XMouseFollowFocusedWindow) as the program to move the mouse.

It also requires to configure the KEYBOARD_ID and ALT_KEYCODE variables like on the other script, but at this point you should be able to change the little amount of script that I'm using to execute the program an change it for something else.

## Dependencies
- xdotool (For both scripts)
- Autokey for the python scripts, unless you run them with something else.
- xinput (For the AutoKey script)
- [xmffw](https://github.com/Vasil-Todorov/XMouseFollowFocusedWindow) (For the xmffw alternative script)

## Extra
While putting the tags for this repository I found this project that you might want to give a try [XMouseFollowFocusedWindow](https://github.com/Vasil-Todorov/XMouseFollowFocusedWindow)
