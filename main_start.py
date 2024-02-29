"""The central program that ties all the modules together."""
from src.modules import pid
from src.modules import global_var
pid.start()

import os
absolutepath = os.path.abspath(__file__)
photo = os.path.dirname(absolutepath)
global_var.photo_path= os.path.join(photo, "assets")
import win32com.client
global dm
dm= win32com.client.Dispatch('dm.dmsoft')
hwnd=global_var.hwnd
def window_xy():
    x1=0
    x2=0
    y1=0
    y2=0
    dm_ret = dm.GetClientRect(hwnd,x1,y1,x2,y2)
    global_var.x1=dm_ret[1]
    global_var.x2=dm_ret[3]
    global_var.y1=dm_ret[2]
    global_var.y2=dm_ret[4]
    return (dm_ret[1],dm_ret[2],dm_ret[3],dm_ret[4])
window_xy()
import time
import subprocess
from src.modules.bot import Bot
from src.modules.capture import Capture
from src.modules.notifier import Notifier
from src.modules.listener import Listener
from src.modules.gui import GUI

from src.modules import memory
from src.modules import runearrow

def start():
    
    bot = Bot()
    capture = Capture()
    notifier = Notifier()
    listener = Listener()
    # memory.start()
    time.sleep(1)
    bot.start()
    while not bot.ready:
        time.sleep(0.01)
    
    capture.start()
    while not capture.ready:
        time.sleep(0.01)
    
    notifier.start()
    while not notifier.ready:
        time.sleep(0.01)
    
    listener.start()
    while not listener.ready:
        time.sleep(0.01)
    
    print('\n[~] Successfully initialized')
    
    gui = GUI()
    gui.start()


start()