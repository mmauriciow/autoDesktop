import subprocess
import driver as dv
from time import sleep

width, height = dv.getSize()

def openDrive():
    driver = subprocess.Popen(["/usr/bin/open", "-n", "-a", "/Applications/Claro drive.app"])

def login(email, password):
    dv.clickOn(width//2 + 130, height//2 - 120, 2)
    dv.moveUp(20)
    dv.clickOn(width//2, height//2 - 5)
    dv.writeEmail(email)
    dv.clickOn(width//2, height//2 + 35)
    dv.write(password)
    dv.moveDown(50)
    dv.clickOn(width//2, height//2 + 150)
    sleep(6)

def closeDrive():
    dv.clickOn(width//4 + 30, height//7 + 10)
