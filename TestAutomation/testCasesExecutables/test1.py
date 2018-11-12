# This test checks that Neovim can create a new file, write a
# basic sentence, and save the file.

import sys
import tempfile
import os
from subprocess import call
import pyautogui

homeDir = os.getenv('HOME')


# Creates and saves a file containing sampleText
def makeWriteFile(sampleText, fileName):
    # Create testFile.txt in home directory
    pyautogui.typewrite('nvim')
    pyautogui.press('space')
    pyautogui.typewrite(homeDir + "/" + fileName)
    pyautogui.press('enter')
    # Enter sampleText, save and quit
    pyautogui.press('i')
    pyautogui.typewrite(sampleText)
    pyautogui.press('enter')
    pyautogui.press('esc')
    pyautogui.typewrite(':wq')
    pyautogui.press('enter')


# Checks that a file has actually been created in home directory
def findFile(fileName):
    found = 0
    # Search home directory for the file
    for dirName, subdirList, fileList in os.walk(homeDir):
        if fileName in fileList:
            found = 1
            print("Test1: Passed (file found!)")
            break  # So it doesn't print "found" multiple times
    if (found == 0):
        print("Test1: Failed (file not found)")


makeWriteFile("This is test 1.", "testFile1.txt")
findFile("testFile1.txt");
