# Opens new nvim file and closes without saving.
# (Test should show that a file was not made)
# This tests the :q! command

import sys
import tempfile
import os
from subprocess import call
import pyautogui

# dirPath is the TestAutomation directory (parent directory of
# parent directory of executing script)
homeDir = os.getenv('HOME')
dirPath = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))


def makeFile(fileName):
    pyautogui.typewrite('nvim')
    pyautogui.press('space')
    pyautogui.typewrite(homeDir + "/" + fileName)
    pyautogui.press('enter')
    pyautogui.press('esc')
    pyautogui.typewrite(':q!')
    pyautogui.press('enter')

def findFile(fileName):
    found = 0
    for root, dirs, files in os.walk(homeDir):
        if fileName in files:
            found = 1
            print("Test3: Failed (the file exists)")
    if (found == 0):
        print("Test3: Passed (the file doesn't exist)")


makeFile("test3.txt")
findFile("test3.txt")
