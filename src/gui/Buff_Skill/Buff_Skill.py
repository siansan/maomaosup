import tkinter as tk
from tkinter import messagebox
from src.gui.interfaces import LabelFrame
from src.common import config, utils
import os
import json
import time
from src.routine.components import Command
from src.common.vkeys import *
import keyboard as kb
import threading
from src.modules import global_var
import re
from datetime import datetime
import cv2
from src.modules import runearrow
from random import random,randint
import gc
import tkinter.ttk as ttk
from src.modules import bot
from src.modules import cv2bg
from src.modules import cv2bg1
import datetime as dt
ok2_=cv2.imread('assets/ok2.jpg', 0)
class Buff_Skill(LabelFrame):

    global jdata,close_data
    filepath="./buff_key_config.txt"
    try:
        if os.path.isfile(filepath):
            f=open("buff_key_config.txt", "r+",encoding='ISO-8859-15')
            data=f.readline()
            jdata=json.loads(data)
            print(jdata["1"])
            f.close()
        else:
            f=open("buff_key_config.txt", "w")
            f.write("")
            f.close()
    except:
        f=open("buff_key_config.txt", "w")
        f.write("")
        f.close()
    try:
        if os.path.isfile("./close_time.txt"):
            f=open("close_time.txt", "r+",encoding='ISO-8859-15')
            data=f.readline()
            close_data=json.loads(data)
            f.close()
        else:
            f=open("close_time.txt", "w")
            f.write('{"0":"True","1":"15:30"}')
            f.close()
    except:
        f=open("close_time.txt", "w")
        f.write('{"0":"True","1":"15:30"}')
        f.close()
    def __init__(self, parent, **kwargs):


        super().__init__(parent, '', **kwargs)
        self.key_0 = tk.Entry(self)
        self.key_0.grid(row=0,column=1)
        try:
            for i in jdata['0'].keys():
                self.key_0.insert(0,i)
        except:
            self.key_0.insert(0,"")

        self.buff_0 = tk.Entry(self)
        self.buff_0.grid(row=0,column=2)
        try:
            for i in jdata['0'].values():
                self.buff_0.insert(0,i)
        except:
            self.buff_0.insert(0,120)

        self.buff_0_text = tk.Label(self,text="輔助技能1(list):")
        self.buff_0_text.grid(row=0,column=0)


        self.key_1 = tk.Entry(self)
        self.key_1.grid(row=1,column=1)
        try:
            for i in jdata['1'].keys():
                self.key_1.insert(0,i)
        except:
            self.key_1.insert(0,"")

        self.buff_1 = tk.Entry(self)
        self.buff_1.grid(row=1,column=2)
        try:
            for i in jdata['1'].values():
                self.buff_1.insert(0,i)
        except:
            self.buff_1.insert(0,120)

        self.buff_1_text = tk.Label(self,text="輔助技能2:")
        self.buff_1_text.grid(row=1,column=0)


        self.key_2 = tk.Entry(self)
        self.key_2.grid(row=2,column=1)
        try:
            for i in jdata['2'].keys():
                self.key_2.insert(0,i)
        except:
            self.key_2.insert(0,"")

        self.buff_2 = tk.Entry(self)
        self.buff_2.grid(row=2,column=2)
        try:
            for i in jdata['2'].values():
                self.buff_2.insert(0,i)
        except:
            self.buff_2.insert(0,120)

        self.buff_2_text = tk.Label(self,text="輔助技能3(無停頓):")
        self.buff_2_text.grid(row=2,column=0)


        self.key_3 = tk.Entry(self)
        self.key_3.grid(row=3,column=1)
        try:
            for i in jdata['3'].keys():
                self.key_3.insert(0,i)
        except:
            self.key_3.insert(0,"")

        self.buff_3 = tk.Entry(self)
        self.buff_3.grid(row=3,column=2)
        try:
            for i in jdata['3'].values():
                self.buff_3.insert(0,i)
        except:
            self.buff_3.insert(0,120)

        self.buff_3_text = tk.Label(self,text="輔助技能4(無停頓):")
        self.buff_3_text.grid(row=3,column=0)


        self.key_4 = tk.Entry(self)
        self.key_4.grid(row=4,column=1)
        try:
            for i in jdata['4'].keys():
                self.key_4.insert(0,i)
        except:
            self.key_4.insert(0,"")

        self.buff_4 = tk.Entry(self)
        self.buff_4.grid(row=4,column=2)
        try:
            for i in jdata['4'].values():
                self.buff_4.insert(0,i)
        except:
            self.buff_4.insert(0,120)

        self.buff_4_text = tk.Label(self,text="消耗1(list):")
        self.buff_4_text.grid(row=4,column=0)


        self.key_5 = tk.Entry(self)
        self.key_5.grid(row=5,column=1)
        try:
            for i in jdata['5'].keys():
                self.key_5.insert(0,i)
        except:
            self.key_5.insert(0,"")

        self.buff_5 = tk.Entry(self)
        self.buff_5.grid(row=5,column=2)
        try:
            for i in jdata['5'].values():
                self.buff_5.insert(0,i)
        except:
            self.buff_5.insert(0,120)

        self.buff_5_text = tk.Label(self,text="消耗2(list):")
        self.buff_5_text.grid(row=5,column=0)


        self.key_6 = tk.Entry(self)
        self.key_6.grid(row=6,column=1)
        try:
            for i in jdata['6'].keys():
                self.key_6.insert(0,i)
        except:
            self.key_6.insert(0,"")

        self.buff_6 = tk.Entry(self)
        self.buff_6.grid(row=6,column=2)
        try:
            for i in jdata['6'].values():
                self.buff_6.insert(0,i)
        except:
            self.buff_6.insert(0,120)

        self.buff_6_text = tk.Label(self,text="消耗3:")
        self.buff_6_text.grid(row=6,column=0)


        self.key_7 = tk.Entry(self)
        self.key_7.grid(row=7,column=1)
        try:
            for i in jdata['7'].keys():
                self.key_7.insert(0,i)
        except:
            self.key_7.insert(0,"")

        self.buff_7 = tk.Entry(self)
        self.buff_7.grid(row=7,column=2)
        try:
            for i in jdata['7'].values():
                self.buff_7.insert(0,i)
        except:
            self.buff_7.insert(0,120)

        self.buff_7_text = tk.Label(self,text="消耗4:")
        self.buff_7_text.grid(row=7,column=0)


        self.key_8 = tk.Entry(self)
        self.key_8.grid(row=8,column=1)
        try:
            for i in jdata['8'].keys():
                self.key_8.insert(0,i)
        except:
            self.key_8.insert(0,"")

        self.buff_8 = tk.Entry(self)
        self.buff_8.grid(row=8,column=2)
        try:
            for i in jdata['8'].values():
                self.buff_8.insert(0,i)
        except:
            self.buff_8.insert(0,120)

        self.buff_8_text = tk.Label(self,text="技能1:")
        self.buff_8_text.grid(row=8,column=0)


        self.key_9 = tk.Entry(self)
        self.key_9.grid(row=9,column=1)
        try:
            for i in jdata['9'].keys():
                self.key_9.insert(0,i)
        except:
            self.key_9.insert(0,"")

        self.buff_9 = tk.Entry(self)
        self.buff_9.grid(row=9,column=2)
        try:
            for i in jdata['9'].values():
                self.buff_9.insert(0,i)
        except:
            self.buff_10.insert(0,120)
        self.buff_10_text = tk.Label(self,text="技能2:")
        self.buff_10_text.grid(row=9,column=0)

        self.key_10 = tk.Entry(self)
        self.key_10.grid(row=10,column=1)
        try:
            for i in jdata['10'].keys():
                self.key_10.insert(0,i)
        except:
            self.key_10.insert(0,"")

        self.buff_10 = tk.Entry(self)
        self.buff_10.grid(row=10,column=2)
        try:
            for i in jdata['10'].values():
                self.buff_10.insert(0,i)
        except:
            self.buff_10.insert(0,120)
        self.buff_10_text = tk.Label(self,text="技能3(不停止):")
        self.buff_10_text.grid(row=10,column=0)

        self.key_11 = tk.Entry(self)
        self.key_11.grid(row=11,column=1)
        try:
            for i in jdata['11'].keys():
                self.key_11.insert(0,i)
        except:
            self.key_11.insert(0,"")

        self.buff_11 = tk.Entry(self)
        self.buff_11.grid(row=11,column=2)

        try:
            for i in jdata['11'].values():
                self.buff_11.insert(0,i)
        except:
            self.buff_11.insert(0,120)
        self.buff_11_text = tk.Label(self,text="技能4(不停止):")
        self.buff_11_text.grid(row=11,column=0)

        self.key_12 = tk.Entry(self)
        self.key_12.grid(row=12,column=1)
        try:
            for i in jdata['12'].keys():
                self.key_12.insert(0,i)
        except:
            self.key_12.insert(0,"")

        self.buff_12 = tk.Entry(self)
        self.buff_12.grid(row=12,column=2)
        try:
            for i in jdata['12'].values():
                self.buff_12.insert(0,i)
        except:
            self.buff_12.insert(0,120)
        self.buff_12_text = tk.Label(self,text="技能5(不停止):")
        self.buff_12_text.grid(row=12,column=0)

        self.var1 = tk.IntVar()

        self.close_text = tk.Checkbutton(self,text="關閉遊戲時間:",variable=self.var1)
        self.close_text.grid(row=15,column=0)

        self.closem = tk.Entry(self)
        self.closem.grid(row=15,column=1)
        self.openm = tk.Entry(self)
        self.openm.grid(row=15,column=2)
        self.closem2 = tk.Entry(self)
        self.closem2.grid(row=15,column=3)
        self.close_day = tk.Entry(self)
        self.close_day.grid(row=15,column=4)
        try:
            self.closem.insert(0,close_data['1'])
            self.openm.insert(0,close_data['2'])
            self.closem2.insert(0,close_data['3'])
            self.close_day.insert(0,close_data['4'])
        except Exception as e:
            print(e)
            self.closem.insert(0,"5:00")


        self.save_key_confing=tk.Button(self,text="儲存",command= lambda self =self: Buff_Skill.save_config(self))
        self.save_key_confing.grid(row=13,column=4)

        self.set_red_text = tk.Label(self,text="紅點設定:")
        self.set_red_text.grid(row=18,column=0)
        self.set_red = tk.Entry(self)
        self.set_red.grid(row=18,column=1)
        self.set_red.insert(0,2)

        self.rune=ttk.Combobox(self, state='readonly')
        self.rune['value']=['shop','logout','tp']
        self.rune.grid(row=19,column=0)
        self.rune.current(0)
        self.rune.bind('<<ComboboxSelected>>', self.items_selected)

        self.channal=ttk.Combobox(self, state='readonly')
        self.channal['value']=['燒','換頻']
        self.channal.grid(row=20,column=0)
        self.channal.current(0)
        self.channal.bind('<<ComboboxSelected>>', self.fire_selected)


        self.skillid = tk.Entry(self)
        self.skillid.grid(row=16,column=0)
        self.skillid_b = tk.Button(self,text='變更Skill_ID',command= lambda self =self: Buff_Skill.change_SkillID(self))
        self.skillid_b.grid(row=16,column=1)

        self.lie_b = tk.Button(self,text='測試測謊',command= lambda self =self: Buff_Skill.lie(self))
        self.lie_b.grid(row=16,column=2)
        # self.sts_thread = threading.Thread(target=self.sts)
        # self.sts_thread.daemon = True
        # self.sts_thread.start()
        self.wt_thread = threading.Thread(target=self.wt)
        self.wt_thread.daemon = True
        self.wt_thread.start()
        self.time = threading.Thread(target=self.close_time)
        self.time.daemon = True
        self.time.start()
    def lie(self):
        runearrow.test_lie()
    def change_SkillID(self):
        try:
            n=int(self.skillid.get())
            runearrow.change_skillid(n)
        except:
            pass
    def save_config(self):
        filepath="./buff_key_config.txt"
        num_dict={}

        for i in range(13):
            key_dict={}
            key_dict[eval(f"self.key_{i}.get()")]=eval(f"self.buff_{i}.get()")
            num_dict[i]=key_dict
        key_dict_str=json.dumps(num_dict)
        if os.path.isfile(filepath):
            f=open("buff_key_config.txt", "w+",encoding='ISO-8859-15')
            f.write(key_dict_str)
            f.close()
        else:
            f=open("buff_key_config.txt", "w+")
            f.write("")
            f.close()
    # def sts(self):
    #     while True:
    #         if kb.is_pressed("f8") and global_var.ss==1:
    #             global_var.ss=2
    #             self.now0=0
    #             self.now1=0
    #             self.now2=0
    #             self.now3=0
    #             self.now4=0
    #             self.now5=0
    #             self.now6=0
    #             self.now7=0
    #             self.now8=0
    #             self.now9=0
    #             time.sleep(1)
    #         time.sleep(0.01)

    def wt(self):
        now=time.time()
        self.now0=0
        self.now1=0
        self.now2=0
        self.now3=0
        self.now4=0
        self.now5=0
        self.now6=0
        self.now7=0
        self.now8=0
        self.now9=0
        self.now10=0
        self.now11=0
        self.now12=0
        count=0
        while True:
                try:
                    if global_var.map_id==runearrow.map_():
                        if global_var.buff_switch==0:
                            if global_var.ss==1:
                                global_var.set_red=int(self.set_red.get())
                                now=time.time()
                                if self.key_0.get()!="":
                                    if (now-self.now0)>(int(self.buff_0.get())) or self.now0==0:
                                        if  global_var.shop==1 and global_var.ss==1:
                                            global_var.rune_stop=1
                                            global_var.stop=True
                                            global_var.buff_stop=1
                                            global_var.jump_attack=0
                                            runearrow.go_shop(0)
                                            time.sleep(3)
                                            key0_list=self.key_0.get().split(",")
                                            for i in key0_list:
                                                    press(i,1,down_time=1)
                                                    time.sleep(0.5)
                                            time.sleep(0.5)
                                            global_var.stop=False
                                            global_var.rune_stop=0
                                            global_var.buff_stop=0
                                            self.now0=now


                                        else:
                                            time.sleep(0.5)


                                if self.key_1.get()!="":
                                    if (now-self.now1)>(int(self.buff_1.get()))or self.now1==0 :
                                        if global_var.ss==1 and global_var.shop==1:
                                            global_var.rune_stop=1
                                            global_var.stop=True
                                            global_var.buff_stop=1
                                            global_var.jump_attack=0
                                            key1_list=self.key_1.get().split(",")
                                            for i in key1_list:
                                                        press(i,1,down_time=1)
                                                        time.sleep(0.1)


                                            self.now1=now
                                            global_var.stop=False
                                            global_var.rune_stop=0
                                            global_var.buff_stop=0

                                        else:
                                            time.sleep(0.5)
                                        # time.sleep(0.5)


                                if self.key_2.get()!="":
                                    if (now-self.now2)>(int(self.buff_2.get()))or self.now2==0:
                                        if global_var.ss==1 and global_var.shop==1:
                                            global_var.stop=True
                                            global_var.rune_stop=1
                                            global_var.buff_stop=1
                                            global_var.jump_attack=0
                                            key2_list=self.key_2.get().split(",")
                                            for i in key2_list:
                                                        press(i,1,down_time=1)
                                                        time.sleep(0.1)
                                            self.now2=now
                                            global_var.stop=False
                                            global_var.rune_stop=0
                                            global_var.buff_stop=0


                                        else:
                                            time.sleep(0.5)


                                if self.key_3.get()!="":
                                    if now-self.now3>(int(self.buff_3.get()))or self.now3==0:
                                        if global_var.ss==1 and global_var.shop==1:
                                            global_var.rune_stop=1
                                            global_var.stop=True
                                            # global_var.buff_stop=1
                                            global_var.jump_attack=0
                                            time.sleep(0.1)
                                            key3_list=self.key_3.get().split(",")
                                            for i in key3_list:
                                                        press(i,1,down_time=1)
                                                        time.sleep(0.1)
                                            self.now3=now
                                            global_var.stop=False
                                            global_var.rune_stop=0
                                            global_var.buff_stop=0

                                            time.sleep(0.5)
                                        else:
                                            time.sleep(0.5)


                                if self.key_4.get()!="":
                                    if now-self.now4>(int(self.buff_4.get()))or self.now4==0:
                                        if global_var.ss==1 and global_var.shop==1:
                                            global_var.rune_stop=1
                                            global_var.stop=True
                                            global_var.buff_stop=1
                                            global_var.jump_attack=0
                                            time.sleep(0.1)
                                            key4_list=self.key_4.get().split(",")
                                            for i in key4_list:
                                                press(i,1,down_time=1)
                                                time.sleep(0.1)
                                            self.now4=now
                                            global_var.stop=False
                                            global_var.rune_stop=0
                                            global_var.buff_stop=0

                                            time.sleep(0.5)
                                                # count+=1
                                        else:
                                            time.sleep(0.5)

                                if self.key_5.get()!="":
                                    if now-self.now5>(int(self.buff_5.get()))or self.now5==0:
                                        if global_var.ss==1 and global_var.shop==1:
                                            global_var.rune_stop=1
                                            global_var.stop=True
                                            global_var.buff_stop=1
                                            global_var.jump_attack=0
                                            # if count<=8:
                                            key5_list=self.key_5.get().split(",")
                                            time.sleep(0.1)
                                            for i in key5_list:
                                                press(i,1,down_time=1)
                                                time.sleep(0.1)
                                            self.now5=now
                                            global_var.stop=False
                                            global_var.rune_stop=0
                                            global_var.buff_stop=0

                                            time.sleep(0.5)
                                                # count+=1
                                        else:
                                            time.sleep(0.5)


                                if self.key_6.get()!="":
                                    if now-self.now6>(int(self.buff_6.get()))or self.now6==0:
                                        if global_var.ss==1 and global_var.shop==1:
                                            global_var.rune_stop=1
                                            global_var.stop=True
                                            global_var.buff_stop=1
                                            global_var.jump_attack=0
                                            time.sleep(0.1)
                                            key6_list=self.key_6.get().split(",")
                                            for i in key6_list:
                                                        press(i,1,down_time=1)
                                                        time.sleep(0.1)
                                            self.now6=now
                                            global_var.stop=False
                                            global_var.rune_stop=0
                                            global_var.buff_stop=0

                                            time.sleep(0.5)
                                        else:
                                            time.sleep(0.5)


                                if self.key_7.get()!="":
                                    if now-self.now7>(int(self.buff_7.get()))or self.now7==0:
                                        if global_var.ss==1 and global_var.shop==1:
                                            global_var.rune_stop=1
                                            global_var.stop=True
                                            global_var.buff_stop=1
                                            global_var.jump_attack=0
                                            runearrow.go_shop(0)
                                            time.sleep(0.5)
                                            key7_list=self.key_7.get().split(",")
                                            for i in key7_list:
                                                        press(i,1,down_time=1)
                                                        time.sleep(0.5)
                                            self.now7=now
                                            global_var.stop=False
                                            global_var.rune_stop=0
                                            global_var.buff_stop=0

                                            time.sleep(0.5)
                                        else:
                                            time.sleep(0.5)


                                if self.key_8.get()!="":
                                    if now-self.now8>(int(self.buff_8.get()))or self.now8==0:
                                        if global_var.ss==1 and global_var.shop==1:
                                            global_var.rune_stop=1
                                            global_var.stop=True
                                            global_var.buff_stop=1
                                            global_var.jump_attack=0
                                            runearrow.go_shop(0)
                                            time.sleep(0.5)
                                            key8_list=self.key_8.get().split(",")
                                            for i in key8_list:
                                                        press(i,1,down_time=1)
                                                        time.sleep(0.5)

                                            self.now8=now
                                            global_var.stop=False
                                            global_var.rune_stop=0
                                            global_var.buff_stop=0

                                            time.sleep(0.5)

                                        else:
                                            time.sleep(0.5)


                                if self.key_9.get()!="":
                                    if now-self.now9>(int(self.buff_9.get()))or self.now9==0:
                                        if global_var.ss==1 and global_var.shop==1:
                                            global_var.rune_stop=1
                                            global_var.stop=True
                                            global_var.buff_stop=1
                                            global_var.jump_attack=0
                                            runearrow.go_shop(0)
                                            time.sleep(0.5)

                                            key9_list=self.key_9.get().split(",")
                                            for i in key9_list:
                                                        press(i,1,down_time=1)
                                                        time.sleep(0.5)
                                            self.now9=now
                                            global_var.stop=False
                                            global_var.rune_stop=0
                                            global_var.buff_stop=0

                                            time.sleep(0.5)
                                        else:
                                            time.sleep(0.5)

                                if self.key_10.get()!="":
                                    if now-self.now10>(int(self.buff_10.get()))or self.now10==0:
                                        if global_var.ss==1 and global_var.shop==1:
                                            key10_list=self.key_10.get().split(",")
                                            for i in key10_list:
                                                        press(i,1,down_time=1)
                                                        time.sleep(0.5)
                                            self.now10=now
                                            time.sleep(0.5)
                                        else:
                                            time.sleep(0.5)

                                if self.key_11.get()!="":
                                    if now-self.now11>(int(self.buff_11.get()))or self.now11==0:
                                        if global_var.ss==1 and global_var.shop==1:
                                            key11_list=self.key_11.get().split(",")
                                            for i in key11_list:
                                                        press(i,1,down_time=1)
                                                        time.sleep(0.5)
                                            self.now11=now
                                            time.sleep(0.5)
                                        else:
                                            time.sleep(0.5)

                                if self.key_12.get()!="":
                                    if now-self.now12>(int(self.buff_12.get()))or self.now12==0:
                                        if global_var.ss==1 and global_var.shop==1:
                                            press(self.key_12.get(),1,down_time=1)
                                            self.now12=now
                                            time.sleep(0.5)
                                        else:
                                            time.sleep(0.5)
                                # print(close_time,self.closem.get())
                                # print(close_time==datetime.strptime(self.closem.get(), "%H:%M").strftime("%H:%M"))


                                if runearrow.fire_()==1:
                                    if global_var.fire_channal==0:
                                        press('end',down_time=1)
                                    elif global_var.fire_channal==1:
                                        global_var.stop==True
                                        bot.change_channel(7)
                                        global_var.stop==False
                            elif global_var.ss==0:
                                time.sleep(1)
                        else:
                            time.sleep(1)
                    else:
                        time.sleep(1)
                except:
                    continue
    def close_time(self):
        while True:
            if self.var1.get()!=1:
                try:
                    tomorrow=dt.date.today()+dt.timedelta(days=int(self.close_day.get()))
                except:
                    time.sleep(1)
            else:
                    close_time=datetime.now().strftime("%m-%d:%H:%M")


                    if self.closem2.get()!="":
                        if close_time>=datetime.strptime(f'{tomorrow}:{self.closem2.get()}', "%Y-%m-%d:%H:%M").strftime('%m-%d:%H:%M'):
                            while True:
                                global_var.close_time=1
                                global_var.ss=0
                                global_var.shop=0
                                runearrow.go_shop(0)
                                press("g", 3, down_time=0.2)
                                mouse_move()
                                frame=cv2bg1.capture(global_var.hwnd)
                                ok2 = utils.multi_match(frame,ok2_,threshold=0.8)
                                if len(ok2)==0:
                                    break
                                elif len(ok2)>0:
                                    runearrow.go_shop(0)
                                    press("enter", 1, down_time=0.5)
                                    time.sleep(0.05)
                        elif self.openm.get()!="":
                                if close_time>=datetime.strptime(f'{tomorrow}:{self.openm.get()}', "%Y-%m-%d:%H:%M").strftime('%m-%d:%H:%M'):
                                    time.sleep(0.3)
                                    target=cv2bg.capture('save.bmp',t=0.8)
                                    if len(target)>0:
                                        click(target, button='left')
                                    time.sleep(0.3)
                                    target=cv2bg.capture('leave_shop.bmp',t=0.8)
                                    if len(target)>0:
                                        click(target, button='left')
                                    else:
                                        mouse_move()

                                    while True:
                                        setting=cv2bg.capture('setting.bmp')

                                        time.sleep(0.3)
                                        if len(setting)>0:
                                            break
                                        else:
                                            mouse_move()
                                        time.sleep(2)
                                        press("t",1,down_time=2)
                        # time.sleep(0.5)
                        # press('f4',down_time=0.5)
                                        global_var.close_time=0
                                        global_var.ss=1
                                        global_var.shop=1

                                        global_var.rune_check=0

                                        gc.collect()
                                elif self.closem.get()!="":
                                    if close_time>=datetime.strptime(f'{tomorrow}:{self.closem.get()}', "%Y-%m-%d:%H:%M").strftime('%m-%d:%H:%M'):
                                        while True:
                                            global_var.close_time=1
                                            global_var.ss=0
                                            global_var.shop=0
                                            runearrow.go_shop(0)
                                            press("g", 3, down_time=0.2)
                                            mouse_move()
                                            frame=cv2bg1.capture(global_var.hwnd)
                                            ok2 = utils.multi_match(frame,ok2_,threshold=0.8)
                                            if len(ok2)==0:
                                                break
                                            elif len(ok2)>0:
                                                runearrow.go_shop(0)
                                                press("enter", 1, down_time=0.5)
                                                time.sleep(0.05)
            time.sleep(1)

    def jump_attack(self,n):
        global_var.jump_attack=n
    def items_selected(self,event):
        n=self.rune.current()
        global_var.rune_select=int(n)
    def fire_selected(self,event):
        n=self.channal.current()
        global_var.fire_channal=int(n)
    def test(self):
        cv2bg.rune_arrow()


