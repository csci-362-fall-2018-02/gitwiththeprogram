import sys
import tempfile
import os
from subprocess import call
import pyautogui



def makeWriteFile():
    pyautogui.typewrite('nvim')
    pyautogui.press('space')
    pyautogui.typewrite('testFile.txt')
    pyautogui.press('enter')

    pyautogui.press('i')
    pyautogui.typewrite('beth is a clone ')
    pyautogui.press('enter')
    pyautogui.press('esc')
    pyautogui.typewrite(':wq!')
    pyautogui.press('enter')

def findFile():
    name = "testFile.txt"
    path = "/home/misae"
    for root, dirs, files in os.walk(path):
        if name in files:
            print("file found!")

makeWriteFile()
findFile();
