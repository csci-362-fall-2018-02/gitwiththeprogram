import sys
import tempfile
import os
from subprocess import call
import pyautogui

# A test to simply make and save a file
#specifically testing x

def makeWriteFile():
    pyautogui.typewrite('nvim')
    pyautogui.press('space')
    pyautogui.typewrite('testFile5.txt')
    pyautogui.press('enter')

    pyautogui.press('i')
    pyautogui.typewrite('some text that is supposed to save ')
    pyautogui.press('enter')
    pyautogui.press('esc')
    pyautogui.typewrite(':x')
    pyautogui.press('enter')

def findFile():
    file = 0
    name = "testFile5.txt"
    path = "."
    for root, dirs, files in os.walk(path):
        if name in files:
            file = 1
            print("Test5: Passed (file found!)")
    if (file == 0):
        print("Test5: Failed (file not found)")

makeWriteFile()
findFile()
