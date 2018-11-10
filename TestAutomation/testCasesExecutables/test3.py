import sys
import tempfile
import os
from subprocess import call
import pyautogui

# a test opens nvim and doesnt save anything
#test should show that a file was not made


def makeFile():

    pyautogui.typewrite('nvim')
    pyautogui.press('space')
    pyautogui.typewrite('justAnotherTest.txt')
    pyautogui.press('enter')
    pyautogui.press('esc')
    pyautogui.typewrite(':q!')
    pyautogui.press('enter')

def findFile():
    name = "justAnotherTest.txt"
    path = "/home/brandi"
    failed = "the file exists: test failure"
    passed = "the file doesnt exist: test passed"
    for root, dirs, files in os.walk(path):
        if name in files:
            print("file found!")

            return failed
        else:

            return passed
makeFile()
print(findFile())
