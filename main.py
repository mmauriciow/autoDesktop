from actions import *
from sys import platform as _platform

if __name__ == '__main__':
    OS = 'MAC_OS' if platform == 'Darwin' else 'Windows'
    print('Running in {} ...'.format(OS))
    openDrive(OS)
    sleep(10)
    login('automationcdemail1@gmail.com', 'Qa123456.', OS)
    closeDrive()