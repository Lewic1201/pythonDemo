import pyautogui
import time
while True:
    time.sleep(60)
    screenWidth, screenHeight = pyautogui.size()
    pyautogui.moveRel(None, 1)
