##passed in the test file by the user and interprets the commands they want
#output a file
#compare the file to the file they submitted
import os, sys
import pyautogui

#reads the file passed as an argument
input_file = open(sys.argv[1])
temp_file = sys.argv[2]
content = input_file.read()
print("testInterpreter.py: using temporary file located at:")
print(temp_file)

#stores each word in the list words
words = content.split()
dir_path = os.path.dirname(os.path.realpath(__file__))
#os.chdir()
#print(dir_path)
#Need to move to temp folder to make output file there

#iterates through the words list
#for word in words:
    #find all the <'s which are commands
    #if "<" in word:
        #type =word[1:]
        #type = type[:-1]
        #pyautogui.press(type)
    #if it has .txt then it is the file they are creating, test1-output.txt
    #this could be where we change the directory
    #elif ".txt" in word:
        #pyautogui.typewrite(word)
        #thought this might be a way to change
        #the directory but not working for me
        # pyautogui.press('enter')
        # pyautogui.press('esc')
        # pyautogui.typewrite(':cd')
        # pyautogui.press('space')
        # pyautogui.typewrite('..')
        # pyautogui.press('enter')
        # pyautogui.typewrite(':cd')
        # pyautogui.press('space')
        # pyautogui.typewrite('temp')
        # pyautogui.press('enter')
    #if not, then plain text
    #else:
        #pyautogui.typewrite(word + ' ')
