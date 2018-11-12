# testing another method to write to a file and quit
# nvim's various commands, in this case 'x' are crucial to it's proper function
# expected output is to confirm that the file does exist

import sys
import tempfile
import os
from subprocess import call
import pyautogui

# creates and writes to the file
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

# confirms that the file does exist
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
