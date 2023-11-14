import keyboard
import time
import threading

# Variable to control the loop
keep_going = True

def check_f1_key():
    global keep_going
    keyboard.wait('F1')
    keep_going = False

# Create and start a new thread that will wait for F1 to be pressed
f1_thread = threading.Thread(target=check_f1_key)
f1_thread.start()

while keep_going:
    # Simulate pressing the '1' key
    keyboard.press_and_release('1')
    # Wait for 0.5 seconds
    time.sleep(0.5)

# Wait for the F1 check thread to finish
f1_thread.join()
