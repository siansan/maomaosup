"""A module for tracking useful in-game information."""
import time
import cv2
import threading
import ctypes
import mss
import mss.windows
import numpy as np
from src.common import config, utils
from ctypes import wintypes
from src.modules import global_var
import re
from src.modules import runearrow
import random
import gc
from src.common.vkeys import press, click,mouse_move,key_down,key_up
user32 = ctypes.windll.user32
user32.SetProcessDPIAware()
# The distance between the top of the minimap and the top of the screen
MINIMAP_TOP_BORDER = 5

# The thickness of the other three borders of the minimap
MINIMAP_BOTTOM_BORDER = 9

# Offset in pixels to adjust for windowed mode
WINDOWED_OFFSET_TOP = 36
WINDOWED_OFFSET_LEFT = 10

# The top-left and bottom-right corners of the minimap
MM_TL_TEMPLATE = cv2.imread('assets/minimap_tl_template.png', 0)
MM_BR_TEMPLATE = cv2.imread('assets/minimap_br_template.png', 0)

MMT_HEIGHT = max(MM_TL_TEMPLATE.shape[0], MM_BR_TEMPLATE.shape[0])
MMT_WIDTH = max(MM_TL_TEMPLATE.shape[1], MM_BR_TEMPLATE.shape[1])

# The player's symbol on the minimap
PLAYER_TEMPLATE = cv2.imread('assets/player_template.png', 0)
PT_HEIGHT, PT_WIDTH = PLAYER_TEMPLATE.shape

class Capture:
    """
    A class that tracks player position and various in-game events. It constantly updates
    the config module with information regarding these events. It also annotates and
    displays the minimap in a pop-up window.
    """

    def __init__(self):
        """Initializes this Capture object's main thread."""
        
        config.capture = self
        self.frame = None
        self.minimap = {}
        self.minimap_ratio = 1
        self.minimap_sample = None
        self.sct = None
        self.window = {
            'left': 0,
            'top': 0,
            'width': 4000,
            'height': 1080
        }

        self.ready = False
        self.calibrated = False
        self.thread = threading.Thread(target=self._main)
        self.thread.daemon = True
        # self.thread1 = threading.Thread(target=self.shootobj)
        # self.thread1.daemon = True
    def start(self):
        """Starts this Capture's thread."""

        print('\n[~] Started video capture')
        self.thread.start()
        # self.thread1.start()
    def _main(self):
        """Constantly monitors the player's position and in-game events."""
        
        while True:
            # Calibrate screen capture
            # self.handle = user32.FindWindowW(None, 'MapleStory')
            # print(self.handle,global_var.hwnd)
            self.handle = global_var.hwnd
            rect = wintypes.RECT()
            user32.GetWindowRect(self.handle, ctypes.pointer(rect))
            rect = (rect.left, rect.top, rect.right, rect.bottom)
            rect = tuple(max(0, x) for x in rect)
            self.window['left'] = rect[0]
            self.window['top'] = rect[1]
            self.window['width'] = max(rect[2] - rect[0], MMT_WIDTH)
            self.window['height'] = max(rect[3] - rect[1], MMT_HEIGHT)
            global_var.window=self.window
            self.calibrated = True
            # Calibrate by finding the top-left and bottom-right corners of the minimap
            
            # config.capture.frame=img_np
            while True:
                runearrow.random_(random.randint(0,50))
                # if global_var.switch==0:
                # if config.enabled:
                #     if global_var.map_id!=runearrow.c_map_():
                #         global_var.black=1
                #         time.sleep(0.1)
                #         press("up",1,down_time=1)
                #         time.sleep(1)
                #         if global_var.map_id==runearrow.c_map_():
                #             press("t",1,down_time=1)
                #             global_var.black=0
                # if config.bot.rune_active:
                #     if global_var.rune_stop==1:
                #         pass
                #     else:
                #         press("f12",n=1)
                # else:
                #     press("f12",n=1)
                config.player_pos = runearrow.xy()
                if not self.calibrated:
                        break
                self.minimap = {
                                # 'minimap': minimap,
                                # 'rune_active': config.bot.rune_active,
                                # 'rune_pos': config.bot.rune_pos,
                                # 'path': config.path,
                                'player_pos': config.player_pos
                            }
                
                # with mss.mss() as self.sct:
                #     global_var.frame = self.screenshot()
                # if global_var.frame is None:
                #     continue
                if not self.ready:
                    self.ready = True
                time.sleep(0.05)
            # if self.frame is None:
            #     continue
            # try:
            #     tl, _ = utils.single_match(self.frame[0:350,0:300], MM_TL_TEMPLATE)
            #     _, br = utils.single_match(self.frame[0:350,0:300], MM_BR_TEMPLATE)
            # except:
            #     continue
            # mm_tl = (
            #     tl[0] + MINIMAP_BOTTOM_BORDER,
            #     tl[1] + MINIMAP_TOP_BORDER
            # )
            # mm_br = (
            #     max(mm_tl[0] + PT_WIDTH, br[0] - MINIMAP_BOTTOM_BORDER),
            #     max(mm_tl[1] + PT_HEIGHT, br[1] - MINIMAP_BOTTOM_BORDER)
            # )
            # self.minimap_ratio = (mm_br[0] - mm_tl[0]) / (mm_br[1] - mm_tl[1])
            # self.minimap_sample = self.frame[mm_tl[1]:mm_br[1], mm_tl[0]:mm_br[0]]
            # self.calibrated = True
                # if not self.ready:
                #             self.ready = True
                # cv2.destroyAllWindows()
                # del img_np,img,self.frame
                # gc.collect()
                # time.sleep(0.0001)
                # with mss.mss() as self.sct:
                #     while True:
                        
                        # if global_var.map_id!=runearrow.map_():
                        #     press("up",1,down_time=1)
                        # runearrow.random_(random.randint(0,50))
                        # if not self.calibrated:
                        #     break

                        # # Take screenshot
                        # self.frame = self.screenshot()
                        # if self.frame is None:
                        #     continue

                        # Crop the frame to only show the minimap
                        # minimap = self.frame[mm_tl[1]:mm_br[1], mm_tl[0]:mm_br[0]]
                        
                        
                        # Package display information to be polled by GUI
                        
                        
                        # global_var.minimap_=minimap
                        # Determine the player's position
                        # player = utils.multi_match(minimap, PLAYER_TEMPLATE, threshold=0.8)
                        # if player:
                        #     config.player_pos = utils.convert_to_relative(player[0], minimap)

                        # Package display information to be polled by GUI
                # self.minimap = {
                #     # 'minimap': minimap,
                #     # 'rune_active': config.bot.rune_active,
                #     # 'rune_pos': config.bot.rune_pos,
                #     # 'path': config.path,
                #     'player_pos': config.player_pos
                # }

                
                    
    def screenshot(self, delay=1):
        try:
            return np.array(self.sct.grab(self.window))
        except mss.exception.ScreenShotError:
            print(f'\n[!] Error while taking screenshot, retrying in {delay} second'
                  + ('s' if delay != 1 else ''))
            time.sleep(delay)
    def screenshot_(sct,window):
        try:
            return np.array(sct.grab(window))
        except mss.exception.ScreenShotError:
            pass
    def shootobj(self):
        while True:
            if config.enabled:
                runearrow.shootobj(1)
                time.sleep(0.3)
                runearrow.shootobj(0)
                time.sleep(0.01)
            else:
                time.sleep(0.5)