import sys
import tempfile
import os
from subprocess import call
import pyautogui

pyautogui.typewrite('nvim')
pyautogui.press('space')
pyautogui.typewrite('testing.txt')
pyautogui.press('enter')
pyautogui.typewrite('wuddup wuddup')
pyautogui.keyDown('esc')
pyautogui.keyUp('esc')
pyautogui.typewrite(':wq!')
pyautogui.keyDown('enter')
pyautogui.keyUp('enter')
