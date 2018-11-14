##passed in the test file by the user and interprets the commands they want
#output a file
#compare the file to the file they submitted
import os, sys
import pyautogui

#reads the file passed as an argument
input_file = open(sys.argv[1])
temp_file = sys.argv[2] ### the full path of temp file string comes in here
content = input_file.read()
print("testInterpreter.py: using temporary file located at:")
print(temp_file)
print("and command file stored at:")
print(sys.argv[1])

#stores each word in the list words
words = content.split()
dir_path = os.path.dirname(os.path.realpath(__file__))

#iterates through the words list
for word in words:
    #find all the <'s which are commands
    if "<" in word:
        type =word[1:]
        type = type[:-1]
        pyautogui.press(type)
    elif ".txt" in word:
        pyautogui.typewrite(temp_file)
    #if not, then plain text
    else:
        pyautogui.typewrite(word)
