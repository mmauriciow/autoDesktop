import subprocess
import driver as dv
from time import sleep
import os
width, height = dv.getSize()

def openDrive(OS):
    if OS == 'MAC_OS':
        driver = subprocess.Popen(["/usr/bin/open", "-n", "-a", "/Applications/Claro drive.app"])
        # os.system()
    else:
        driver = subprocess

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
    print('Exit...')