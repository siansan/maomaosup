# 變更標籤內容
from src.modules import global_var
import win32com.client
import time
rune_dict={0:"down",1:"up",2:"left",3:"right"}
ms="MapleStory.exe"
global dm,hwnd,sw

dm= win32com.client.Dispatch('dm.dmsoft')
hwnd=global_var.hwnd
sw=0
def arrow():
    rune_list=[]

    try:
        arrow01=dm.ReadInt(hwnd,'13FFF0800',0)
        arrow02=dm.ReadInt(hwnd,'13FFF0804',0)
        arrow03=dm.ReadInt(hwnd,'13FFF0808',0)
        arrow04=dm.ReadInt(hwnd,'13FFF080C',0)
        rune_list.append(rune_dict[arrow01])
        rune_list.append(rune_dict[arrow02])
        rune_list.append(rune_dict[arrow03])
        rune_list.append(rune_dict[arrow04])
        return rune_list
    except:
        pass

def go_shop(s):
    try:
        dm.WriteInt(hwnd,'13FFF0810',0,s)
    except:
        pass
# def switch_auto(s):
#     try:
#         dm.WriteInt(hwnd,'13FFF0840',0,s)
#     except:
#         pass
def red_():
    try:
        red=dm.ReadInt(hwnd,'13FFF0814',0)
        return red
    except:
        pass
def fire_():
    try:
        red=dm.ReadInt(hwnd,'13FFF081C',0)
        return red
    except:
        pass
def rune_debuff():
    try:
        red=dm.ReadInt(hwnd,'13FFF0820',0)
        return red
    except:
        pass
def map_():
    try:
        red=dm.ReadInt(hwnd,'13FFF082C',0)
        return red
    except:
        pass
def c_map_():
    try:
        # pymem=Pymem(ms)
        red=dm.ReadInt(hwnd,'13FFF082C',0)
        # pymem.close_process()
        return red
    except:
        pass
def action_():
    try:
        red=dm.ReadInt(hwnd,'13FFF0830',0)
        return red
    except:
        pass
def monster_():
    try:
        red=dm.ReadInt(hwnd,'13FFF0818',0)
        return red
    except:
        pass
def set_red_():
    try:
        red=dm.ReadInt(hwnd,'13FFF0838',0)
        return red
    except:
        pass
def set_monster_():
    try:
        red=dm.ReadInt(hwnd,'13FFF083C',0)
        return red
    except:
        pass
def random_(s):
    try:
        dm.WriteInt(hwnd,'13FFF0844',0,s)
    except:
        pass
def xy():
    try:
        # pymem=Pymem(ms)
        x=dm.ReadInt(hwnd,'13FFF0854',0)
        y=dm.ReadInt(hwnd,'13FFF097C',0)
        # pymem.close_process()
        return (x,y)
    except:
        pass
def rune_xy():
    try:
        x=dm.ReadInt(hwnd,'13FFF0AA4',0)
        y=dm.ReadInt(hwnd,'13FFF0BBC',0)   
        return (x,y)
    except:
        pass
def switch_():
    global sw
    if sw==0:
        dm.WriteInt(hwnd,'13FFF0810',0,1)
        dm.WriteInt(hwnd,'13FFF0840',0,1)
        sw=1
    else:
        dm.WriteInt(hwnd,'13FFF0810',0,0)
        dm.WriteInt(hwnd,'13FFF0840',0,0)
        sw=0
def shootobj(s):
        dm.WriteInt(hwnd,'13FFF0824',0,s)
def change_skillid(s):
    dm.WriteInt(hwnd,'13FFF0CEC',0,s)
def switch_13FFF0CF0(s):
    dm.WriteInt(hwnd,'13FFF0CF0',0,s)
def switch_shootobj():
    dm.WriteInt(hwnd,'13FFF0D0E',0,0)
    time.sleep(0.3)
    dm.WriteInt(hwnd,'13FFF0D0E',0,1)
def test_lie():
    dm.WriteInt(hwnd,'13FFF0CF4',0,1)
    time.sleep(0.1)
    dm.WriteInt(hwnd,'13FFF0CF4',0,0)
def lie():
    try:
        x=dm.ReadInt(hwnd,'13FFF0CF8',0) 
        return (x)
    except:
        pass
def faketime_reset(s):
    dm.WriteInt(hwnd,'13FFF0D16',0,s)
def lie():
    dm.ReadInt(hwnd,'13FFF0D1A',0)


def target():
    dm.WriteInt(hwnd,'13FFF0D22',0,1)

def high_jump(s):
    dm.WriteInt(hwnd,'13FFF0D26',0,int(s))