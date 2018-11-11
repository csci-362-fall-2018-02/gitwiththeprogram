
import sys
import tempfile
import os
from subprocess import call
import pyautogui


os.chdir("/home/brandi/Desktop/github/gitwiththeprogram/TestAutomation/testCasesExecutables")
def makeWriteFile():
    #print(sys.path)
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
    os.chdir("/home/brandi/Desktop/github/gitwiththeprogram/TestAutomation/scripts")
    file = 0
    name = "testFile.txt"
    path = "."
    for dirName, subdirList, fileList in os.walk(path):
        #print(fileList)
        if name in fileList:
            file = 1
            print("Test1: Passed (file found!)")
    if (file ==0):
        print("Test1: Filed (file not found)")

makeWriteFile()
findFile();
