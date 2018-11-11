import sys
import tempfile
import os
from subprocess import call
import pyautogui

#os.chdir("/home/brandi/Desktop/github/gitwiththeprogram/TestAutomation/testCasesExecutables")
# A test to add lines to a file and check if it wrote correctly
def readExistingFile():
    os.chdir("/home/brandi/Desktop/github/gitwiththeprogram/TestAutomation/scripts")
    fileToRead = open("testFile.txt", "r")
    existingLines = fileToRead.read()
    return existingLines
def addToFile():
    os.chdir("/home/brandi/Desktop/github/gitwiththeprogram/TestAutomation/scripts")
    pyautogui.typewrite('nvim')
    pyautogui.press('space')
    pyautogui.typewrite('testFile.txt')
    pyautogui.press('enter')

    pyautogui.press('o')
    lineWritten = 'beth is just crazy, shes not a clone'
    pyautogui.typewrite(lineWritten)
    pyautogui.press('enter')
    pyautogui.press('esc')
    pyautogui.typewrite(':wq!')
    pyautogui.press('enter')

existingText = readExistingFile()
addToFile()

def compareLines():
    os.chdir("/home/brandi/Desktop/github/gitwiththeprogram/TestAutomation/scripts")
    failed = "the lines do no match"
    passed = "lines match-Test Passed"
    newText = readExistingFile()
    if (existingText == newText):
        return passed
    else:
        return failed
compareLines()
print(compareLines())
