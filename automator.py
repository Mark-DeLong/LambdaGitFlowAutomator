#!/usr/bin/env python

import os

def getData():
    userName = raw_input("Enter your github username: ")

    f = open("./userData.txt", "w")
    f.write(userName)
    f.close()

    saveDirectory = raw_input("Enter the Directory where you want to save your files (Desktop/subfolder; Documents/subfolder)): ")

    f = open("./saveDirectory.txt", "w")
    f.write(saveDirectory)
    f.close

    choice2 = input("Press 1 to Exit, or 2 to Load the Program: ")

    if choice2 == 2:
        repo = raw_input("Enter the name of the project: ")
        
        os.system('cd && cd ' + saveDirectory + ' && git clone https://github.com/' + userName + '/' + repo + ' && cd ' + repo + ' && git checkout -b ' + userName + ' && code .')
    else:
        exit()

choice1 = input("Press 1 to set your data, or 2 to Load the Program: ")

if choice1 == 1:
    getData()
else:
    f = open("./userData.txt", "r")
    userName = f.read()
    f.close()

    f = open("./saveDirectory.txt", "r")
    saveDirectory = f.read()
    f.close()

    repo = raw_input("Enter the name of the project: ")

    os.system('cd && cd ' + saveDirectory + ' && git clone https://github.com/' + userName + '/' + repo + ' && cd ' + repo + ' && git checkout -b ' + userName + ' && code .')