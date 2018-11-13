##passed in the test file by the user and interprets the commands they want
#output a file
#compare the file to the file they submitted
import os, sys
import pyautogui

input_file = open(sys.argv[1])
content = input_file.read()
print(content)
