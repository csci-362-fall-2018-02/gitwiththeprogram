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
    file = 0
    name = "justAnotherTest.txt"
    path = "."
    failed = "Test3: Failed (the file exists)"
    passed = "Test3: Passed (the file doesnt exist)"
    for root, dirs, files in os.walk(path):
        if name in files:
            #print("file found!")
            file = 1
            print(passed)
            #return failed
        #else:
            #return passed
    if(file ==0):
        print(failed)


makeFile()
findFile()
