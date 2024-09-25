# AutoKey script to use with xmffw.

# It's designed to use alt tab so I could alt tab and execute the script
# If you want to use it run (xinput list) search for your keyboard id and put it down below
# Now run (xpinut test Your_KeyBoard_ID) and it look for the code of your alt

# Replace with your actual keyboard ID and Alt keycode
KEYBOARD_ID = "Your keyboard ID goes here"
ALT_KEYCODE = "The code for alt"

# Hold Alt and cycle windows with Tab
subprocess.run(["xdotool", "keydown", "Alt"])  # Hold Alt
subprocess.run(["xdotool", "key", "Tab"])      # Press Tab to cycle windows

# Wait until the Alt key is released using xinput
while True:
    # Get xinput events to check for Alt release
    xinput_output = subprocess.run(["xinput", "query-state", KEYBOARD_ID], capture_output=True, text=True).stdout
    
    # Look for the key release of the Alt key
    if f"key[{ALT_KEYCODE}]=up" in xinput_output:
        break  # Exit the loop when Alt is released

    time.sleep(0.1)  # Sleep for a short time and check again

# Once Alt is released, get the new active window
subprocess.run(["xdotool", "keyup", "Alt"])  # Release Alt
subprocess.run(["xmffw"])                    # Execute xmffw
