from pynput.mouse import Button, Controller
import time

mouse = Controller()

waitTime = 0.135
pause = False

def PositionDetect():
    PreviousPos = mouse.position
    if mouse.position == PreviousPos:
        print("Mouse position has not changed. Clicking.")
        pause = False
        return True
        Clicker()
    elif mouse.position != PreviousPos:
        print("Mouse has moved. Aborting clicker.")
        pause = True
        Clicker()
    time.sleep(waitTime)
    PreviousPos = mouse.position
    Clicker()

def Clicker():
        print("Current position: ", str(mouse.position))
        time.sleep(waitTime)
        if PositionDetect():
            while True:
                mouse.click(Button.left, 1)
                time.sleep(0.1)
                PositionDetect()
        elif PositionDetect == False:
            PositionDetect()

print("Initialising...")
Clicker()
