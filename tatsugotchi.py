
import pyperclip
import sys
import pyautogui
import time
import random

sys.setrecursionlimit(99999999)

message = 't!tg train'

def smart():
    x = 0
    time.sleep(4)
    pyperclip.copy(message)
    while True:
        time.sleep(13)
        pyautogui.keyDown('ctrl')
        pyautogui.typewrite('v')
        pyautogui.keyUp('ctrl')
        pyautogui.typewrite('\n')
        x += 1
        if x == 2500:
            pyautogui.keyDown('ctrl')
            pyautogui.typewrite('r')
            pyautogui.keyUp('ctrl')
            x = 0

print('type smart() and enter to start')
