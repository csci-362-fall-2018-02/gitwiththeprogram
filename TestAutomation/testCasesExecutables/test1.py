
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
    os.chdir("/home/Desktop/github/gitwiththeprogram")
    name = "testFile.txt"
    path = "."
    for dirName, subdirList, fileList in os.walk(path):
        #print(fileList)
        if name in fileList:
            print("file found!")

makeWriteFile()
findFile();
