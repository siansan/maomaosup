# 變更標籤內容
from pynput import keyboard
import pymem


global s
s=0


def p(switch):
    p=pymem.Pymem("MapleStory.exe")
    p.write_int(0x13FFF0810,switch)
    p.write_int(0x13FFF0840,switch)
    p.write_int(0x13FFF0CF0,switch)
    p.close_process()
        
def on_press(key):
    if key == keyboard.Key.f3:
        global s
        if s==0:
            p(1)
            s=1
        else:
            p(0)
            s=0

        
def on_release(key):
    pass

listener=keyboard.Listener(on_press=on_press,on_release=on_release)
listener.daemon=True
listener.start()



listener.join()
