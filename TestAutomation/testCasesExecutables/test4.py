# nvim core function involves writing to a file properly
# specifically testing the ability to write ('i') save ('w') then quit ('q')

import sys
import tempfile
import os
from subprocess import call
import pyautogui

# creating the file, and writing 'aw geez rick' to that file 
def makeWriteFile():
    pyautogui.typewrite('nvim')
    pyautogui.press('space')
    pyautogui.typewrite('testFile4.txt')
    pyautogui.press('enter')

    pyautogui.press('i')
    pyautogui.typewrite('aw geez rick ')
    pyautogui.press('enter')
    pyautogui.press('esc')
    pyautogui.typewrite(':wq')
    pyautogui.press('enter')

# searching for and finding that file
def findFile():
    found = 0
    name = "testFile4.txt"
    path = "."
    for root, dirs, files in os.walk(path):
        if name in files:
            found = 1
            print("Test4: Passed (file found!)")
    if (found ==0):
        print("Test4: Failed (File not found)")

makeWriteFile()
findFile()
