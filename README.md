GitWithTheProgram 362 Final Project GitHub
=========================================

## Members: 
Brandi Durham  
Lauren Tubbs  
Misae Evans   
John Quinn  

----
Instructions on how to download and run our test cases. For this project we used Ubuntu 16.04 and Python version 2.7, which comes preinstalled on Ubuntu.  
1. Clone our github repository using the command git clone **`https://github.com/csci-362-fall-2018-02/gitwiththeprogram.git`**
2. Run the following commands to install prerequisites for Neovim and make Neovim.  
**`sudo apt-get install ninja-build gettext libtool libtool-bin autoconf automake cmake g++ pkg-config unzip`**  
**`git clone https://github.com/neovim/neovim`**  
**`cd neovim`**  
**`make`**  
**`sudo make install`**   
Make sure you have python installed by running the command:  
**`python -V`**  
Installing pip  
**`sudo apt-get install python-setuptools python-dev build-essential`**
**`sudo easy_install pip`**
Installing PyAutoGUI  
**`pip install python-xlib`**  
**`sudo apt-get install scrot`**  
**`sudo apt-get install python-tk`**  
**`sudo apt-get install python-dev`**  
**`pip install pyautogui`**  
3. Move to the TestAutomation folder
4. Run testing script: **Make sure and add the '&' to the end of the command**  
**`./scripts/runAllTests.sh&`**  

----

