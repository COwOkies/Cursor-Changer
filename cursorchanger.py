import win32con
import ctypes
import psutil
import time
from win32gui import GetWindowText, GetForegroundWindow, FindWindow, LoadImage
from win32process import GetWindowThreadProcessId

def change_cursor(pathcurseur):
    cursor = LoadImage(0, pathcurseur, win32con.IMAGE_CURSOR, 
                                0, 0, win32con.LR_LOADFROMFILE);
    ctypes.windll.user32.SetSystemCursor(cursor, 32512)
    ctypes.windll.user32.DestroyCursor(cursor);

import configparser

config = configparser.ConfigParser()
config.read('config.ini')

w_name = config.get('values','Program')
timesleep = config.getfloat('values','TimeSleep')
DefaultCursor = config.get('values','DefaultCursorName')
NewCursor = config.get('values','NewCursorName')

isdefault=True

pid = None
while pid == None:
    for proc in psutil.process_iter():
        if w_name in proc.name():
           pid = proc.pid
           break
    if pid == None:
        print(f"{w_name} wasn't found, please open {w_name}", end='\r')
    time.sleep(1)
print(f"Found {w_name}: {pid}{' '*22}{' '*len(w_name)}")

while True:
    n_pid = GetWindowThreadProcessId(GetForegroundWindow())[1]
    if n_pid == pid:
        if isdefault == True:
            change_cursor(NewCursor)
            isdefault = False
            print(w_name,"is focused")
    else:
        if isdefault == False:
            change_cursor(DefaultCursor)
            isdefault = True
            print(w_name,"isn't focused")
    time.sleep(timesleep)


