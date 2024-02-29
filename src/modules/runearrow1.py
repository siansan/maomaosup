# 變更標籤內容
from pymem import Pymem
import time
rune_dict={0:"down",1:"up",2:"left",3:"right"}
ms="MapleStory.exe"

def arrow():
    rune_list=[]

    try:
        pymem=Pymem(ms)
        arrow01=pymem.read_int(0x13FFF0800)
        arrow02=pymem.read_int(0x13FFF0804)
        arrow03=pymem.read_int(0x13FFF0808)
        arrow04=pymem.read_int(0x13FFF080C)
        rune_list.append(rune_dict[arrow01])
        rune_list.append(rune_dict[arrow02])
        rune_list.append(rune_dict[arrow03])
        rune_list.append(rune_dict[arrow04])
        pymem.close_process()
        return rune_list
    except:
        pass

def go_shop(s):
    try:
        pymem=Pymem(ms)
        pymem.write_int(0x13FFF0810,s)
        pymem.close_process()
    except:
        pass
def in_skill():
    try:
        pymem=Pymem(ms)
        red=pymem.read_int(0x13FFF0810)
        pymem.close_process()
        return red
    except:
        pass
def red_():
    try:
        pymem=Pymem(ms)
        red=pymem.read_int(0x13FFF0814)
        pymem.close_process()
        return red
    except:
        pass
def fire_():
    try:
        pymem=Pymem(ms)
        red=pymem.read_int(0x13FFF081C)
        pymem.close_process()
        return red
    except:
        pass
def rune_debuff():
    try:
        pymem=Pymem(ms)
        red=pymem.read_bytes(0x13FFF0820,1)
        pymem.close_process()
        return red
    except:
        pass
def lie():
    try:
        pymem=Pymem(ms)
        pymem.write_int(0x13FFF0824,1)
        time.sleep(0.1)
        pymem.write_int(0x13FFF0824,0)
        pymem.close_process()
    except:
        pass
def map_():
    try:
        pymem=Pymem(ms)
        red=pymem.read_int(0x13FFF082C)
        pymem.close_process()
        return red
    except:
        pass
def action_():
    try:
        pymem=Pymem(ms)
        red=pymem.read_int(0x13FFF0830)
        pymem.close_process()
        return red
    except:
        pass
def monster_():
    try:
        pymem=Pymem(ms)
        red=pymem.read_int(0x13FFF0818)
        pymem.close_process()
        return red
    except:
        pass
def set_red_():
    try:
        pymem=Pymem(ms)
        red=pymem.read_int(0x13FFF0838)
        pymem.close_process()
        return red
    except:
        pass
def set_monster_():
    try:
        pymem=Pymem(ms)
        red=pymem.read_int(0x13FFF083C)
        pymem.close_process()
        return red
    except:
        pass
def random_(s):
    try:
        pymem=Pymem(ms)
        pymem.write_int(0x13FFF0844,s)
        pymem.close_process()
    except:
        pass
def xy():
    try:
        pymem=Pymem(ms)
        x=pymem.read_int(0x13FFF0854)
        y=pymem.read_int(0x13FFF097C)
        pymem.close_process()
        return (x,y)
    except:
        pass

# def rune_tpye():
#     mem = Pymem(ms)
#     try:
#         address=0x13FFF0848
#         offsets=[0x20,0x0]
#         addrrune=mem.read_int(address)
#         for offset in offsets:
#             addrrune = mem.read_int(addrrune + offset)
#         addrrune+=addrrune
#         mem.write_int(0x13FFF0984,addrrune)
#         mem.close_process()
#     except:
#         mem.close_process()
def rune_xy():
    mem = Pymem(ms)
    try:
        address=0x13FFF0848
        offsets=[0x20,0x0]
        addrrune=mem.read_int(address)
        for offset in offsets:
            addrrune = mem.read_int(addrrune + offset)
        addrrune+=addrrune
        offsets_xy=[0x08,eval(f"0x{addrrune}*8+0x8"),0x70]
        offset_x=[0x50]
        offset_y=[0x54]
        rune_=mem.read_int(address)
        for offset in offsets_xy:
            rune_ = mem.read_int(rune_ + offset)
        rune_x=mem.read_int(rune_ + offset_x[0])
        rune_y=mem.read_int(rune_ + offset_y[0])
        mem.write_int(0x13FFF084C,rune_x)
        mem.write_int(0x13FFF0850,rune_y)
        mem.close_process()
        return (rune_x,rune_y)
    except:
        mem.close_process()
# def rune_xy():
#     try:
#         pymem=Pymem(ms)
#         x=pymem.read_int(0x13FFF084C)
#         y=pymem.read_int(0x13FFF0850)
#         pymem.close_process()
#         return (x,y)
#     except:
#         pass
def write_mapid(s):
    try:
        pymem=Pymem(ms)
        pymem.write_int(0x13FFF0828,s)
        pymem.close_process()
    except:
        pass