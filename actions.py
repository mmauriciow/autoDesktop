import subprocess
import driver as dv
from time import sleep
import os
# from pywinauto.application import Application
width, height = dv.getSize()

def openDrive(OS):
    if OS == 'MAC_OS':
        os.system('open /Applications/Claro\ drive.app/')
    else:
        # Application().start(r'C:\Program Files (x86)\Claro drive\Claro drive.exe')
        sleep(5)

def login(email, password, OS):
    dv.clickOn(width//2 + 130, height//2 - 120, 2)
    dv.moveUp(20)
    dv.clickOn(width//2, height//2 - 5)
    dv.writeEmail(email, OS)
    dv.clickOn(width//2, height//2 + 35)
    dv.write(password)
    dv.moveDown(50)
    dv.clickOn(width//2, height//2 + 150)
    sleep(12)

def closeDrive(OS):
    dv.clickOn(width//4 + 30, height//7 + 10)
    if OS == 'MAC_OS':
        os.system("pkill Claro drive")
    else: 
        os.system('TASKKILL /F /IM "Claro drive.exe')
    print('Exit...')