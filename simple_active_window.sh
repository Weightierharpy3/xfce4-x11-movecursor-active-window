#!/bin/bash
# This is a simple bash script for simply moving the cursor to the active window
# Get the active window ID
active_window=$(xdotool getactivewindow)

# Get the window's geometry: width, height, and position
eval "$(xdotool getwindowgeometry --shell "$active_window")"

# Calculate the center of the window
center_x=$((X + WIDTH / 2))
center_y=$((Y + HEIGHT / 2))

# Move the mouse to the center of the window
xdotool mousemove $center_x $center_y
