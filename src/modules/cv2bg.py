import win32com.client
import os
from src.modules import global_var
import cv2
global dm
dm= win32com.client.Dispatch('dm.dmsoft')
dm_ret = dm.Reg('646842f3dd42de689d8e2b1ab1778cd9e204fa','0001')
hwnd=global_var.hwnd
gdi = "dx2"
mouse = "dx.mouse.position.lock.api|dx.mouse.clip.lock.api|dx.mouse.input.lock.api|dx.mouse.state.api|dx.mouse.api|dx.mouse.cursor"
keyboard = "dx.keypad.input.lock.api|dx.keypad.state.api|dx.keypad.api"
public = "dx.public.active.api"
dm.BindWindowEx(hwnd,gdi,mouse,keyboard,public,0)
dm.SetPath(global_var.photo_path)
# dm.SetPath('/assets')
def window_xy():
    x1=0
    x2=0
    y1=0
    y2=0
    dm_ret = dm.GetClientRect(hwnd,x1,y1,x2,y2)
    global_var.x1=dm_ret[1]
    global_var.x2=dm_ret[3]
    global_var.y1=dm_ret[2]
    global_var.x2=dm_ret[4]
    return (dm_ret[1],dm_ret[2],dm_ret[3],dm_ret[4])

def capture(p,t=0.9,x2=global_var.x2,y2=global_var.y2):
    dm_ret = dm.FindPicEx(0, 0, x2, y2,p,"20",t,0)
    return (dm_ret)
window_xy()
def rune_arrow():
    dm.CaptureJpg(455, 170, 583, 298, "C:/Users/sian/Desktop/test/new_mem_nobg/arrow_pic/0.jpg", 100)
    dm.CaptureJpg(555, 170, 683, 298, "C:/Users/sian/Desktop/test/new_mem_nobg/arrow_pic/1.jpg", 100)
    dm.CaptureJpg(655, 170, 783, 298, "C:/Users/sian/Desktop/test/new_mem_nobg/arrow_pic/2.jpg", 100)
    dm.CaptureJpg(755, 170, 883, 298, "C:/Users/sian/Desktop/test/new_mem_nobg/arrow_pic/3.jpg", 100)
