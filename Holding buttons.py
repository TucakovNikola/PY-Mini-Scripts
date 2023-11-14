import pyautogui
import keyboard
import time

# Wait for 2 seconds before starting the script
time.sleep(2)

# Hold down the letter 'W'
keyboard.press('w')

# Hold down the left mouse button
pyautogui.mouseDown(button='left')

# Wait for the user to stop the script by pressing F1
keyboard.wait('F1')

# Release the letter 'W'
keyboard.release('w')

# Release the left mouse button
pyautogui.mouseUp(button='left')
