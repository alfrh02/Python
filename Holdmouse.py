from pynput.mouse import Button, Controller
import time

mouse = Controller()

time.sleep(3)

mouse.press(Button.left)
