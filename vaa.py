import win32com.client
from src.modules import global_var
global dm
global_var.var()
dm= win32com.client.Dispatch('dm.dmsoft')
dm_ret = dm.Reg('646842f3dd42de689d8e2b1ab1778cd9e204fa','0001')
hwnd=15077182
gdi = "dx2"
mouse = "dx.mouse.position.lock.api|dx.mouse.clip.lock.api|dx.mouse.input.lock.api|dx.mouse.state.api|dx.mouse.api|dx.mouse.cursor"
keyboard = "dx.keypad.input.lock.api|dx.keypad.state.api|dx.keypad.api"
public = "dx.public.active.api"
x=dm.BindWindowEx(hwnd,gdi,mouse,keyboard,public,0)
print(x)
dm.SetPath('C:/Users/sian/Desktop/test/new_mem_nobg/assets')
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

def capture(p,t=0.65,x2=global_var.x2,y2=global_var.y2):
    dm_ret = dm.FindPicEx(0, 0, 4000, 4000,p,'20',t,0)
    return (dm_ret)
# print(window_xy())
print(capture('setting.bmp',t=0.8))