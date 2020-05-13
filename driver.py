import pyautogui as py

            #       Wrapper for pyautogui

def clickOn(x, y, clk = 1):
    py.moveTo(x, y)
    py.click(clicks = clk)

def writeEmail(email):
    user, domain = email.split('@')
    py.write(user, 0.1)
    py.hotkey('alt', '2')
    py.write(domain, 0.1)

def write(text):
    py.write(text, 0.1)

def getSize():
    return py.size()

def moveDown(y = 50):
    py.scroll(-y)

def moveUp(y = 50):
    py.scroll(y)
