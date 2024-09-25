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

## Dependencies
- xdotool (For both scripts)
- xinput (For the AutoKey script)
