import pyautogui
import keyboard
import time

while not keyboard.is_pressed('F5'):
    pyautogui.keyDown('F')
    time.sleep(2)
    pyautogui.keyUp('F')
    time.sleep(0.5)

# Cleanup
keyboard.unhook_all()
F