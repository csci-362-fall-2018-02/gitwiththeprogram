# Checks that Neovim can add lines to an existing file.

import sys
import tempfile
import os
from subprocess import call
import pyautogui
import filecmp

# dirPath is the TestAutomation directory (parent directory of
# parent directory of executing script)
homeDir = os.getenv('HOME')
dirPath = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))


def readExistingFile(fileName):
    fileToRead = open(fileName, "r")
    existingLines = fileToRead.readlines()
    fileToRead.close()
    return existingLines


def addToFile(sampleText, fileName):
    # Opens fileName
    pyautogui.typewrite('nvim')
    pyautogui.press('space')
    pyautogui.typewrite(fileName)
    pyautogui.press('enter')
    # Writes sample text to file
    pyautogui.press('o')
    pyautogui.typewrite(sampleText)
    pyautogui.press('enter')
    pyautogui.press('esc')
    pyautogui.typewrite(':wq')
    pyautogui.press('enter')


# Compares two files to see if content is the same
def compareLines(file1, file2):
    if (filecmp.cmp(file1, file2)):
        print("Passed (lines match)")
    else:
        print("Failed (the lines do not match)")


# Copy test2-append (in testCases) so it can be restored after
originalFile = readExistingFile(dirPath +
    "/testCases/test2-append.txt")

# Appends some text to test2-append
addToFile("Second line.",
    dirPath + "/testCases/test2-append.txt")

# Compare to file with the correct text
compareLines(dirPath + "/testCases/test2-correct.txt",
    dirPath + "/testCases/test2-append.txt")

# Restore original text of test2-append
f = open(dirPath + "/testCases/test2-append.txt", "w")
f.writelines(originalFile)
f.close()
