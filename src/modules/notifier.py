"""A module for detecting and notifying the user of dangerous in-game events."""

from src.common import config, utils
import time
import os
import cv2
import pygame
import threading
import numpy as np
import mss
import keyboard as kb
from src.routine.components import Point
from src.common.vkeys import press, click,mouse_move, key_down, key_up
from src.modules import global_var
from src.modules import runearrow
from ctypes import wintypes
import ctypes
import requests
from datetime import datetime
from src.modules import bot
import gc
from tkinter import messagebox
from src.modules import cv2bg
from src.modules import cv2bg1
from src.modules import pid
user32 = ctypes.windll.user32
user32.SetProcessDPIAware()
# A rune's symbol on the minimap
RUNE_RANGES = (
    ((141, 148, 245), (146, 158, 255)),
)
rune_filtered = utils.filter_color(cv2.imread('assets/rune_template.png'), RUNE_RANGES)
RUNE_TEMPLATE = cv2.cvtColor(rune_filtered, cv2.COLOR_BGR2GRAY)

# Other players' symbols on the minimap
OTHER_RANGES = (
    ((0, 245, 215), (10, 255, 255)),
)
# other_filtered = utils.filter_color(cv2.imread('assets/other_template.png'), OTHER_RANGES)
# OTHER_TEMPLATE = cv2.cvtColor(other_filtered, cv2.COLOR_BGR2GRAY)

# The distance between the top of the minimap and the top of the screen
MINIMAP_TOP_BORDER = 5

# The thickness of the other three borders of the minimap
MINIMAP_BOTTOM_BORDER = 9

# Offset in pixels to adjust for windowed mode
WINDOWED_OFFSET_TOP = 36
WINDOWED_OFFSET_LEFT = 10
MM_TL_TEMPLATE = cv2.imread('assets/minimap_tl_template.png', 0)
MM_BR_TEMPLATE = cv2.imread('assets/minimap_br_template.png', 0)

MMT_HEIGHT = max(MM_TL_TEMPLATE.shape[0], MM_BR_TEMPLATE.shape[0])
MMT_WIDTH = max(MM_TL_TEMPLATE.shape[1], MM_BR_TEMPLATE.shape[1])
PLAYER_TEMPLATE = cv2.imread('assets/player_template.png', 0)
PT_HEIGHT, PT_WIDTH = PLAYER_TEMPLATE.shape

# The Elite Boss's warning sign
ELITE_TEMPLATE = cv2.imread('assets/elite_template.jpg', 0)
fiola_template=cv2.imread('assets/fiola.jpg', 0)
ok_=cv2.imread('assets/ok.jpg', 0)
stop_=cv2.imread('assets/stop.jpg', 0)
ok3_=cv2.imread('assets/ok3.jpg', 0)
def get_alert_path(name):
    return os.path.join(Notifier.ALERTS_DIR, f'{name}.mp3')


class Notifier:
    ALERTS_DIR = os.path.join('assets', 'alerts')
    def lineNotifyMessage(self):

        headers = {
            "Authorization": "Bearer T6RsFJDvbGaI13JGciu3l5HLgS1ky5r6BONCEbJ8997", 
            "Content-Type" : "application/x-www-form-urlencoded"
        }
        fiola_time=datetime.now()
        fiola_time=fiola_time.strftime("%H:%M")
        payload = {'message': f"{fiola_time} :本機非歐娜測謊中!!!!" }
        requests.post("https://notify-api.line.me/api/notify", headers = headers, params = payload)

    def lineNotifyMessage_map(self):

        headers = {
            "Authorization": "Bearer T6RsFJDvbGaI13JGciu3l5HLgS1ky5r6BONCEbJ8997", 
            "Content-Type" : "application/x-www-form-urlencoded"
        }
        fiola_time=datetime.now()
        fiola_time=fiola_time.strftime("%H:%M")
        payload = {'message': f"{fiola_time} :本機真實之房!!!!" }
        requests.post("https://notify-api.line.me/api/notify", headers = headers, params = payload)

    def lineNotifyMessage_MS(self):

        headers = {
            "Authorization": "Bearer T6RsFJDvbGaI13JGciu3l5HLgS1ky5r6BONCEbJ8997", 
            "Content-Type" : "application/x-www-form-urlencoded"
        }
        fiola_time=datetime.now()
        fiola_time=fiola_time.strftime("%H:%M")
        payload = {'message': f"{fiola_time} :本機斷線!!!!" }
        requests.post("https://notify-api.line.me/api/notify", headers = headers, params = payload)
    def __init__(self):
        """Initializes this Notifier object's main thread."""

        pygame.mixer.init()
        self.red_count=0
        self.titles = set()
        self.mixer = pygame.mixer.music
        self.minimap_ratio = 1
        self.sct = None
        self.thread = threading.Thread(target=self._main)
        self.thread.daemon = True
        self.thread1 = threading.Thread(target=self.rune_)
        self.thread1.daemon = True
        self.rune_alert_delay = 270         # 4.5 minutes
    def start(self):
        """Starts this Notifier's thread."""

        print('\n[~] Started notifier')
        self.thread.start()
        self.thread1.start()
    def _main(self):
        self.ready = True
        count=0
        
        while True:
            #if global_var.shop!=0:
            if config.enabled:
                # Check for unexpected black screen
                # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                # if np.count_nonzero(gray < 15) / height / width > self.room_change_threshold:
                #     config.enabled=False
                #     self._alert('siren')
                # Check for elite warning
                # elite_frame = frame[height // 4:3 * height // 4, width // 4:3 * width // 4]
                # elite = utils.multi_match(elite_frame, ELITE_TEMPLATE, threshold=0.9)
                # if len(elite) > 0:
                #     self._alert('siren')
                if runearrow.lie()==1:
                    self._ping('ding')
                if runearrow.map_()==993073000:
                    self.lineNotifyMessage_map()
                    break
                pid.clean_start()
                if global_var.hwnd:
                    pass
                else:
                    self.lineNotifyMessage_MS()
                    break
                while True:
                    if runearrow.red_()>global_var.set_red:
                        count+=1
                        global_var.red_stop=1
                        self._ping('ding')
                        time.sleep(1)
                        if count>=45:
                            self.red_count+=1
                            if self.red_count>=3:
                                command = 'taskkill /F /IM MapleStory.exe'
                                os.system(command)
                                messagebox.showinfo('關閉','紅點')
                            bot.change_channel(0)
                            count=0
                    else:
                        count=0
                        break
                if global_var.map_id==runearrow.map_():
                    if runearrow.red_()==runearrow.set_red_():
                            
                        # frame=cv2bg.capture(global_var.hwnd)
                        # ok3 = utils.multi_match(frame,ok3_,threshold=0.6)
                        # if ok3:
                        #     ok3_pos = min(ok3, key=lambda p: p[0])
                        #     target = (
                        #         round(ok3_pos[0] + global_var.window['left']),
                        #         round(ok3_pos[1] + global_var.window['top'])
                        #     )
                            target=cv2bg.capture('Cancel.bmp')
                            if len(target)>0:
                                if target[0]!=-1:
                                    click(target, button='right')
                            target=cv2bg.capture('ok3.bmp')
                            if len(target)>0:
                                if target[0]!=-1:
                                    click(target, button='left')
                                    time.sleep(3)
                                    global_var.stop=True
                                    time.sleep(0.5)
                                    press('t',1,down_time=1)
                                    time.sleep(0.5)
                                    global_var.stop=False
                
        
                
                # print(321)
                if global_var.fiola_check==0:
                    # img = pyautogui.screenshot(region=[0,0,1920,1080])
                    # img = cv2.cvtColor(np.asarray(img), cv2.COLOR_RGB2BGR)
                    # img_np = np.array(img)
                    frame=cv2bg1.capture(global_var.hwnd)
                    fiola = utils.multi_match(frame,fiola_template,threshold=0.8)
                    # fiola=cv2bg.capture('fiola.bmp',t=0.7)
                    # fiola=cv2bg.capture('setting.bmp',t=0.7)
                    # print(fiola,123)
                    if len(fiola) > 0:
                        # config.enabled=False
                        # global_var.ss=0
                        self.lineNotifyMessage()
                        sound_thread = threading.Thread(target=self.sound_)
                        sound_thread.daemon = True
                        sound_thread.start()
                    del frame,fiola
                    gc.collect()
                
                
                    # img = pyautogui.screenshot(region=[0,0,1920,1080])
                    # img = cv2.cvtColor(np.asarray(img), cv2.COLOR_RGB2BGR)
                    # img_np = np.array(img)
                    
                    frame=cv2bg1.capture(global_var.hwnd)
                    stop = utils.multi_match(frame,stop_,threshold=0.8)
                    if len(stop)>0:
                        press('esc')
            time.sleep(1)
                    #     while True:
                    #         frame = cv2bg.capture(global_var.hwnd)
                    #         ok = utils.multi_match(frame,ok_,threshold=0.8)
                    #         if len(ok) > 0:
                    #             global_var.ss=1
                    #             config.enabled=True
                    #             break
                    # frame = cv2bg.capture(global_var.hwnd)
                    # ok = utils.multi_match(frame,ok_,threshold=0.8)
                    # if len(ok) > 0:
                    #     key_up("alt")
                    #     press("esc", 1, down_time=0.1)
                    # frame = cv2bg.capture(global_var.hwnd)
                    # stop = utils.multi_match(frame,stop_,threshold=0.8)
                    # if len(stop) > 0:
                    #     key_up("alt")
                    #     press("esc", 1, down_time=0.1)
                    # Check for other players entering the map
                    # filtered = utils.filter_color(minimap, OTHER_RANGES)
                    # others = len(utils.multi_match(filtered, OTHER_TEMPLATE, threshold=0.5))
                    # config.stage_fright = others > 0
                    # if others != prev_others:
                        # if others > prev_others:
                    
                            # prev_others = others
               

            
    def rune_(self):
        count=0
        while True:
            try:
             # Check for rune
                if config.enabled:
                    if global_var.close_time==0:
                        if global_var.channel==0:
                            if global_var.map_id==runearrow.map_():
                                if runearrow.rune_debuff()==0:
                                    # time.sleep(10)
                            
                                    config.bot.rune_pos = runearrow.rune_xy()
                                    # if config.bot.rune_pos[0]==0 and config.bot.rune_pos[1]==0:
                                    #     pass
                                    # elif global_var.rune_x==config.bot.rune_pos[0] and global_var.rune_y==config.bot.rune_pos[1]:
                                    #     pass
                                    # else:
                                    if global_var.rune_check!=1:
                                        
                                        # Calibrate by finding the top-left and bottom-right corners of the minimap
                                        # img = pyautogui.screenshot(region=[100,100,1920,1080])
                                        # img = cv2.cvtColor(np.asarray(img), cv2.COLOR_RGB2BGR)
                                        # img_np = np.array(img)
                                        self.frame=cv2bg1.capture(global_var.hwnd)
                                    
                                        tl, t1 = utils.single_match(self.frame, MM_TL_TEMPLATE)
                                        t2, br = utils.single_match(self.frame, MM_BR_TEMPLATE)

                                        mm_tl = (
                                            tl[0] + MINIMAP_BOTTOM_BORDER,
                                            tl[1] + MINIMAP_TOP_BORDER
                                        )
                                        mm_br = (
                                            max(mm_tl[0] + PT_WIDTH, br[0] - MINIMAP_BOTTOM_BORDER),
                                            max(mm_tl[1] + PT_HEIGHT, br[1] - MINIMAP_BOTTOM_BORDER)
                                        )
                                        self.minimap_ratio = (mm_br[0] - mm_tl[0]) / (mm_br[1] - mm_tl[1])
                                        self.minimap_sample = self.frame[mm_tl[1]:mm_br[1], mm_tl[0]:mm_br[0]]
                                        f=utils.filter_color(self.minimap_sample,RUNE_RANGES)
                                        rune = utils.multi_match(f, RUNE_TEMPLATE, threshold=0.6)
                                        count+=1
                                        if count>300:
                                            press('left')

                                        if len(rune) > 0:
                                            # global_var.rune_x=config.bot.rune_pos[0]
                                            # global_var.rune_y=config.bot.rune_pos[1]
                                            config.bot.rune_active = True
                                            global_var.rune_check=1
                                            global_var.switch=0
                                            print("解輪開始")
                                            del rune,self.frame,tl, t1,t2, br,f#self.minimap_ratio,self.minimap_sample,f,mm_tl,mm_br
                                            gc.collect()
                                            count=0
                                    count+=1 
                                
                time.sleep(1)
                
            except:
                time.sleep(0.5)
                pass
    def _alert(self, name, volume=0.75):
        """
        Plays an alert to notify user of a dangerous event. Stops the alert
        once the key bound to 'Start/stop' is pressed.
        """

        config.enabled = False
        config.listener.enabled = False
        self.mixer.load(get_alert_path(name))
        self.mixer.set_volume(volume)
        self.mixer.play(-1)
        while not kb.is_pressed(config.listener.config['Start/stop']):
            time.sleep(0.1)
        self.mixer.stop()
        time.sleep(2)
        config.listener.enabled = True
    def sound_(self):
        global_var.fiola_check=1
        time.sleep(60)
        global_var.fiola_check=0
    def _ping(self, name, volume=0.5):
        """A quick notification for non-dangerous events."""

        self.mixer.load(get_alert_path(name))
        self.mixer.set_volume(volume)
        self.mixer.play()
    def fiola_thread(self):
        config.enabled==False
        time.sleep(50)
        config.enabled==True
        global_var.fiola_check=0
#################################
#       Helper Functions        #
#################################
def distance_to_rune(point):
    """
    Calculates the distance from POINT to the rune.
    :param point:   The position to check.
    :return:        The distance from POINT to the rune, infinity if it is not a Point object.
    """

    if isinstance(point, Point):
        return utils.distance(config.bot.rune_pos, point.location)
    return float('inf')
