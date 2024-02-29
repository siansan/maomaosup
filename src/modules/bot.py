"""An interpreter that reads and executes user-created routines."""
import threading
import time
# import git
import cv2
from os.path import splitext, basename
from src.common import config, utils
from src.routine import components
from src.routine.routine import Routine
from src.command_book.command_book import CommandBook
from src.routine.components import Point
from src.common.vkeys import press, click,mouse_move,key_down,key_up
from src.common.interfaces import Configurable
from src.modules import global_var
from src.modules import runearrow
from ctypes import wintypes
import ctypes
from src.modules.capture import Capture
from random import random
import gc
import numpy as np
from src.modules import cv2bg
from src.modules import cv2bg1
import mss
from random import randint
ok2_=cv2.imread('assets/ok2.jpg', 0)
# The rune's buff icon
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
RUNE_BUFF_TEMPLATE = cv2.imread('assets/rune_buff_template.jpg', 0)
leave_shop=cv2.imread('assets/leave_shop.jpg', 0)
cc=cv2.imread('assets/change_channal.jpg', 0)
unfind_rune=cv2.imread('assets/rune_template.jpg', 0)
setting_=cv2.imread('assets/setting.jpg', 0)
enter_=cv2.imread('assets/enter.jpg', 0)
shop_=cv2.imread('assets/shop.jpg', 0)
MM_TL_TEMPLATE = cv2.imread('assets/minimap_tl_template.png', 0)
MM_BR_TEMPLATE = cv2.imread('assets/minimap_br_template.png', 0)
MMT_HEIGHT = max(MM_TL_TEMPLATE.shape[0], MM_BR_TEMPLATE.shape[0])
MMT_WIDTH = max(MM_TL_TEMPLATE.shape[1], MM_BR_TEMPLATE.shape[1])
PLAYER_TEMPLATE = cv2.imread('assets/player_template.png', 0)
PT_HEIGHT, PT_WIDTH = PLAYER_TEMPLATE.shape
class Bot(Configurable):
    """A class that interprets and executes user-defined routines."""

    DEFAULT_CONFIG = {
        'Interact': 'y',
        'Feed pet': '9'
    }

    def __init__(self):
        """Loads a user-defined routine on start up and initializes this Bot's main thread."""

        super().__init__('keybindings')
        config.bot = self
        self.capture=Capture()
        self.rune_active = False
        self.rune_pos = (0, 0)
        self.rune_closest_pos = (0, 0)      # Location of the Point closest to rune
        self.submodules = []
        self.command_book = None            # CommandBook instance
        self.red_count=0
        # self.module_name = None
        # self.buff = components.Buff()

        # self.command_book = {}
        # for c in (components.Wait, components.Walk, components.Fall,
        #           components.Move, components.Adjust, components.Buff):
        #     self.command_book[c.__name__.lower()] = c

        config.routine = Routine()
        self.ready = False
        self.thread = threading.Thread(target=self._main)
        self.thread.daemon = True
    def start(self):
        """
        Starts this Bot object's thread.
        :return:    None
        """

        # self.update_submodules()
        print('\n[~] Started main bot loop')
        self.thread.start()
    def _main(self):
        """
        The main body of Bot that executes the user's routine.
        :return:    None
        """

        print('\n[~] Initializing detection algorithm:\n')
        # model = detection.load_model()
        print('\n[~] Initialized detection algorithm')
        self.ready = True
        config.listener.enabled = True
        last_fed = time.time()
        while True:
            gc.collect()
            if global_var.map_id==runearrow.map_():
                if global_var.black==0:
                    if not runearrow.red_()>2:
                        if global_var.close_time==0:
                            if config.enabled:
                                # Buff and feed pets
                                # self.command_book.buff.main()
                                # hwnd = win32gui.FindWindow(0,"MapleStory")
                                # win32gui.SetForegroundWindow(hwnd)
                                # pet_settings = config.gui.settings.pets
                                # auto_feed = pet_settings.auto_feed.get()
                                # num_pets = pet_settings.num_pets.get()
                                # now = time.time()
                                # if auto_feed and now - last_fed > 1200 / num_pets:
                                #     press(self.config['Feed pet'], 1)
                                #     last_fed = now
                                # Highlight the current Point
                                
                                # if runearrow.read_walk()==0:
                                #     press('left',down_time=2)
                                #     runearrow.walk(1)
                                # Execute next Point in the routine
                                # if runearrow.fire_()==0:
                                #     if global_var.channel==0:
                                #         if runearrow.rune_debuff()==b'\x00':
                                #             if global_var.fiola_check==0:
                                #                 time.sleep(10)
                                #                 config.bot.rune_pos = runearrow.rune_xy()
                                #                 # if config.bot.rune_pos[0]==0 and config.bot.rune_pos[1]==0:
                                #                 #     pass
                                #                 # elif global_var.rune_x==config.bot.rune_pos[0] and global_var.rune_y==config.bot.rune_pos[1]:
                                #                 #     pass
                                #                 # else:
                                                
                                #                 minimap = config.capture.minimap['minimap']
                                #                 # Calibrate by finding the top-left and bottom-right corners of the minimap
                                #                 filtered = utils.filter_color(minimap, RUNE_RANGES)
                                #                 rune = utils.multi_match(filtered, RUNE_TEMPLATE, threshold=0.9)
                                #                 print(rune)
                                #                 if len(rune) > 0:
                                #                     # global_var.rune_x=config.bot.rune_pos[0]
                                #                     # global_var.rune_y=config.bot.rune_pos[1]
                                #                     config.bot.rune_active = True
                                #                     global_var.rune_check=1
                                #                     print("解輪開始")
                                #                     self._solve_rune()
                                #                     del rune,#self.frame,tl, t1,t2, br,f#self.minimap_ratio,self.minimap_sample,f,mm_tl,mm_br
                                #                     gc.collect()
                                                
                                if  global_var.stop==False:
                                    config.gui.view.routine.select(config.routine.index)
                                    config.gui.view.details.display_info(config.routine.index)
                                    element = config.routine[config.routine.index]
                                    if self.rune_active :#and isinstance(element, Point) :#and element.location == self.rune_closest_pos
                                        global_var.ss=0
                                        if global_var.rune_select==0:
                                            self.shop_solve_rune()
                                            
                                        elif global_var.rune_select==1:
                                            self.logout_solve_rune()

                                        elif global_var.rune_select==2:
                                            self.tp_solve_rune()

                                    if global_var.black==0:
                                        element.execute()
                                        config.routine.step()
                                    # if runearrow.action_()>=12:
                                    #     while True:
                                    #         key_down("up")
                                    #         time.sleep(0.5)
                                    #         if not runearrow.action_()>=12:
                                    #             key_up("up")
                                    #             break
                                    # if global_var.map_id==runearrow.map_():
                                        
                                        # time.sleep(0.01 + 0.05 * random())
                            else:
                                time.sleep(0.1)
                        else:
                            time.sleep(0.1)
                    else:
                        time.sleep(0.1)
                                        
                else:
                    time.sleep(0.1)
            else:
                    time.sleep(0.1)

                              
                                
                                 
              
            
    

    @utils.run_if_enabled
    def logout_solve_rune(self):
        """
        Moves to the position of the rune and solves the arrow-key puzzle.
        :param model:   The TensorFlow model to classify with.
        :param sct:     The mss instance object with which to take screenshots.
        :return:        None
        """
        count=0
        global_var.ss=0
        global_var.shop=0
        runearrow.go_shop(0)
        # runearrow.go_shop(1)  
        while True:   
            if self.red_count>=1 and runearrow.red_()>global_var.set_red:
                self.rune_active = False
                global_var.rune_stop=0
                global_var.ss=1
                global_var.shop=1
                runearrow.go_shop(0)
                global_var.rune_check=0
                change_channel(7)
                self.red_count=0
                count=0
                return 0
            if runearrow.rune_debuff()==1:
                    break  
            if count>0 and count%2==0:
                while True:
                    time.sleep(0.3)
                    frame = cv2bg.capture(global_var.hwnd)
                    mouse_move()
                    setting = utils.multi_match(frame,
                                                    setting_,
                                                    threshold=0.9)
                    if setting:
                        setting_pos = min(setting, key=lambda p: p[0])
                        target = (
                            round(setting_pos[0] + global_var.window['left']),
                            round(setting_pos[1] + global_var.window['top'])
                        )

                        click(target, button='left')
                    else:
                        break
                    del setting
                    gc.collect()
                    while True:
                        if global_var.fiola_check==0:
                            time.sleep(1)
                            press('up')
                            press('enter')
                            time.sleep(0.5)
                            press('enter')
                            time.sleep(3)
                            break
                        else:
                            time.sleep(1)
                    while True:
                        frame=cv2bg.capture(global_var.hwnd)
                        enter = utils.multi_match(frame,enter_,threshold=0.8)
                        time.sleep(0.05)
                        if len(enter)>0:
                            time.sleep(0.5)
                            press("enter", 1, down_time=0.5)
                            
                            break
                        else:
                            mouse_move()
                    del enter
                    
                    # time.sleep(5)
                    # while True:
                    #     time.sleep(0.3)
                    #     frame = cv2bg.capture(global_var.hwnd)
                    #     mouse_move()
                    #     leave = utils.multi_match(frame,
                    #                                     leave_shop,
                    #                                     threshold=0.7)
                    #     print(leave)
                    #     if leave:
                    #         leave_pos = min(leave, key=lambda p: p[0])
                    #         target = (
                    #             round(leave_pos[0] + global_var.window['left']),
                    #             round(leave_pos[1] + global_var.window['top'])
                    #         )

                    #         click(target, button='left')
                            
                    #         break
                    #     else:
                    #         mouse_move()
                            
                    #     time.sleep(0.05)
                    # del leave,frame,rune_buff
                    # gc.collect()
                    while True:
                        frame=cv2bg.capture(global_var.hwnd)
                        setting = utils.multi_match(frame,setting_,threshold=0.8)
                        time.sleep(0.3)
                        if len(setting)>0:
                            break
                        else:
                            mouse_move()
                    del setting
                    time.sleep(1)
                    press('page down')
                    time.sleep(0.5)
                    press('6')
                    time.sleep(0.5)
                    press('delete')
                    time.sleep(0.1)
                    press('esc')
                    self.red_count+=1
                    count=0
                    
                    break
            
            if runearrow.rune_debuff()==0:
                # move = self.command_book['move']
                # move(*self.rune_pos).execute()
                for i in range(3):
                    adjust = self.command_book['adjust']
                    adjust(*self.rune_pos).execute()
                global_var.rune_stop=1
                press(self.config['Interact'], 1, down_time=0.5)        # Inherited from Configurable

                print('\nSolving rune:')
                inferences = []
                # for _ in range(15):
                # frame = config.capture.frame
                solution=runearrow.arrow()
                # solution = detection.merge_detection(model, frame)
                # if solution:
                #     print(', '.join(solution))
                #     if solution in inferences:
                #         print('Solution found, entering result')
                print(solution)
                time.sleep(2)
                for arrow in solution:
                    press(arrow, 1, down_time=0.1)
                time.sleep(1)
                global_var.rune_stop=0
                count+=1
        if runearrow.rune_debuff()==1:
            time.sleep(0.3)
            for _ in range(3):
                time.sleep(0.01)
                frame = cv2bg.capture(global_var.hwnd)
                rune_buff = utils.multi_match(frame[:frame.shape[0] // 5, :],
                                                RUNE_BUFF_TEMPLATE,
                                                threshold=0.5)
                print(rune_buff)
                if rune_buff:
                    rune_buff_pos = min(rune_buff, key=lambda p: p[0])
                    target = (
                        round(rune_buff_pos[0] + global_var.window['left']),
                        round(rune_buff_pos[1] + global_var.window['top'])
                    )
                    print(target)
                    click(target, button='right')
                else:
                    break
                while True:
                    frame=cv2bg.capture(global_var.hwnd)
                    setting = utils.multi_match(frame,setting_,threshold=0.8)
                    time.sleep(0.3)
                    if len(setting)>0:
                        break
                    else:
                        mouse_move()
                del setting
            time.sleep(0.5)
            press("t",1,down_time=2)
            time.sleep(0.5)
            press('f4',down_time=0.5)
            
            self.rune_active = False
            global_var.rune_stop=0
            global_var.ss=1
            global_var.shop=1
            runearrow.go_shop(1)
            global_var.rune_check=0
            self.red_count=0
            del frame,rune_buff
            gc.collect()
            return 0
                    # if count==9:
                    #     self.rune_active = False
                    #     global_var.shop=1
                    #     runearrow.go_shop(0)
                    #     runearrow.walk(1)
                    #     global_var.rune_check=0
                    #     global_var.rune_x=0
                    #     global_var.rune_y=0
                        
                    #     count=0
                    #     break
                    
              
                    
                        # press("`", 3, down_time=0.2)
                        # mouse_move()
                        # img = pyautogui.screenshot(region=[0,0,1920,1080])
                        # img = cv2.cvtColor(np.asarray(img), cv2.COLOR_RGB2BGR)
                        # img_np = np.array(img)
                        # frame=cv2bg.capture(global_var.hwnd)
                        # ok2 = utils.multi_match(frame,ok2_,threshold=0.8)
                        # time.sleep(0.05)
                        # if len(ok2)>0:
                        #     press("enter", 1, down_time=0.5)
                        #     time.sleep(0.05)
                        # else:
                        #     del ok2
                        #     gc.collect()
                        #     break
    def shop_solve_rune(self):
        """
        Moves to the position of the rune and solves the arrow-key puzzle.
        :param model:   The TensorFlow model to classify with.
        :param sct:     The mss instance object with which to take screenshots.
        :return:        None
        """
        count=0
        global_var.ss=0
        global_var.shop=0
        runearrow.go_shop(0)
        runearrow.switch_13FFF0CF0(0)
        runearrow.faketime_reset(1)
        # runearrow.go_shop(1) 
        while True:   
            if self.red_count>=1 and runearrow.red_()>global_var.set_red and global_var.map_id==runearrow.map_():
                self.rune_active = False
                global_var.rune_stop=0
                global_var.ss=1
                global_var.shop=1
                runearrow.go_shop(0)
                runearrow.switch_13FFF0CF0(0)
                global_var.rune_check=0
                change_channel(7)
                self.red_count=0
                count=0
                return 0
            if runearrow.rune_debuff()==1:
                    break  
            if count>2 and count%1==0:
            # if count>0 and count%1==0:
                while True:
                    print('shop')
                    press("f11")
                    while True:
                        if global_var.fiola_check==0:
                            # while True:
                            #     if runearrow.lie()==0:
                            #         time.sleep(1)
                            #         break
                            #     else:
                            #         time.sleep(1)
                            
                            press("g", 3, down_time=0.2)
                            mouse_move()
                            frame=cv2bg1.capture(global_var.hwnd)
                            ok2 = utils.multi_match(frame,ok2_,threshold=0.8)
                            # time.sleep(0.05)
                            # shop_1 = utils.multi_match(frame,
                            #                             shop_,
                            #                             threshold=0.9)
                        
                            # if shop_1:
                            #     shop_pos = min(shop_1, key=lambda p: p[0])
                            #     target = (
                            #         round(shop_pos[0] + global_var.window['left']),
                            #         round(shop_pos[1] + global_var.window['top'])
                            #     )
                            #     print(target)
                            #     click(target, button='left')
                            #     break
                            if len(ok2)==0:
                                break
                            elif len(ok2)>0:
                                runearrow.go_shop(0)
                                press("enter", 1, down_time=0.5)
                                time.sleep(0.05)
                            # else:
                            #     mouse_move()
                            
                            
                        else:
                            time.sleep(1)
                    time.sleep(5)
                    
                        # frame = cv2bg.capture(global_var.hwnd)
                        # mouse_move()
                        # leave_shop_ = utils.multi_match(frame,
                        #                                 leave_shop,
                        #                                 threshold=0.7)
                        
                        # if leave_shop_:
                        #     leave_shop_pos = min(leave_shop_, key=lambda p: p[0])
                        #     target = (
                        #         round(leave_shop_pos[0] + global_var.window['left']),
                        #         round(leave_shop_pos[1] + global_var.window['top'])
                        #     )
                    target=cv2bg.capture('save.bmp',t=0.8)
                    if len(target)>0:
                        click(target, button='left')
                    time.sleep(0.3)
                    target=cv2bg.capture('leave_shop.bmp',t=0.8)
                    print(target)
                    if len(target)>0:
                        click(target, button='left')
                        break

          
                    while True:
                        frame=cv2bg1.capture(global_var.hwnd)
                        setting = utils.multi_match(frame,setting_,threshold=0.8)
                        
                        time.sleep(0.3)
                        if len(setting)>0:
                            break
                        else:
                            mouse_move()
                    press("f11")
                    self.red_count+=1
                    count=0
                    break
                    # time.sleep(5)
                    # while True:
                    #     time.sleep(0.3)
                    #     frame = cv2bg.capture(global_var.hwnd)
                    #     mouse_move()
                    #     leave = utils.multi_match(frame,
                    #                                     leave_shop,
                    #                                     threshold=0.7)
                    #     print(leave)
                    #     if leave:
                    #         leave_pos = min(leave, key=lambda p: p[0])
                    #         target = (
                    #             round(leave_pos[0] + global_var.window['left']),
                    #             round(leave_pos[1] + global_var.window['top'])
                    #         )

                    #         click(target, button='left')
                            
                    #         break
                    #     else:
                    #         mouse_move()
                            
                    #     time.sleep(0.05)
                    # del leave,frame,rune_buff
                    # gc.collect()
            
            if runearrow.rune_debuff()==0:
                # move = self.command_book['move']
                # move(*self.rune_pos).execute()
                runearrow.target()
                while True:
                    adjust = self.command_book['adjust']
                    adjust(*self.rune_pos).execute()
                    if abs(config.bot.rune_pos[0]- config.player_pos[0])<30 and abs(config.bot.rune_pos[1]- config.player_pos[1])<=3:
                        break
                time.sleep(1)
                global_var.rune_stop=1
                press(self.config['Interact'], 1, down_time=1)        # Inherited from Configurable
                print('\nSolving rune:')
                inferences = []
                # for _ in range(15):
                # frame = config.capture.frame
                #runearrow.rune_arrow_adr()
                time.sleep(1)
                solution=runearrow.arrow()
                # solution = detection.merge_detection(model, frame)
                # if solution:
                #     print(', '.join(solution))
                #     if solution in inferences:
                #         print('Solution found, entering result')
                print(solution)
                time.sleep(1)
                for arrow in solution:
                    press(arrow, 1, down_time=0.1)
                time.sleep(0.5)
                global_var.rune_stop=0
                count+=1
        if runearrow.rune_debuff()==1:
            for _ in range(3):
                target=cv2bg.capture('rune_buff_template.bmp',t=0.9,y2=global_var.y2//15)
                # frame = cv2bg.capture(global_var.hwnd)
                # rune_buff = utils.multi_match(frame[:frame.shape[0] // 5, :],
                #                                 RUNE_BUFF_TEMPLATE,
                #                                 threshold=0.5)
                # print(rune_buff)
                # if rune_buff:
                #     rune_buff_pos = min(rune_buff, key=lambda p: p[0])
                #     target = (
                #         round(rune_buff_pos[0] + global_var.window['left']),
                #         round(rune_buff_pos[1] + global_var.window['top'])
                #     )
                #     print(target)
                if len(target)>0:
                    try:
                        target=target.split('|')
                        for i in target:
                            click(i, button='right')
                            time.sleep(0.001)
                    except:
                        for i in target:
                            click(i, button='right')
                            time.sleep(0.001)
                while True:
                    frame=cv2bg1.capture(global_var.hwnd)
                    setting = utils.multi_match(frame,setting_,threshold=0.8)
                    time.sleep(0.3)
                    if len(setting)>0:
                        break
                    else:
                        mouse_move()
            self.rune_active = False
            global_var.rune_stop=0
            global_var.ss=1
            global_var.shop=1
            global_var.rune_check=0
            runearrow.go_shop(1)
            self.red_count=0
            runearrow.faketime_reset(0)
            gc.collect()
            return 0
                    # if count==9:
                    #     self.rune_active = False
                    #     global_var.shop=1
                    #     runearrow.go_shop(0)
                    #     runearrow.walk(1)
                    #     global_var.rune_check=0
                    #     global_var.rune_x=0
                    #     global_var.rune_y=0
                        
                    #     count=0
                    #     break
                    
              
                    
                        # press("`", 3, down_time=0.2)
                        # mouse_move()
                        # img = pyautogui.screenshot(region=[0,0,1920,1080])
                        # img = cv2.cvtColor(np.asarray(img), cv2.COLOR_RGB2BGR)
                        # img_np = np.array(img)
                        # frame=cv2bg.capture(global_var.hwnd)
                        # ok2 = utils.multi_match(frame,ok2_,threshold=0.8)
                        # time.sleep(0.05)
                        # if len(ok2)>0:
                        #     press("enter", 1, down_time=0.5)
                        #     time.sleep(0.05)
                        # else:
                        #     del ok2
                        #     gc.collect()
                        #     break
                
                    
                    
    def load_commands(self, file):
        try:
            self.command_book = CommandBook(file)
            config.gui.settings.update_class_bindings()
        except ValueError:
            pass    # TODO: UI warning popup, say check cmd for errors


    def tp_solve_rune(self):
        """
        Moves to the position of the rune and solves the arrow-key puzzle.
        :param model:   The TensorFlow model to classify with.
        :param sct:     The mss instance object with which to take screenshots.
        :return:        None
        """
        count=0
        global_var.ss=0
        global_var.shop=0
        runearrow.go_shop(0)
        runearrow.switch_13FFF0CF0(0)
        runearrow.faketime_reset(1)
        # runearrow.go_shop(1) 
        while True:   
            if self.red_count>=1 and runearrow.red_()>global_var.set_red and global_var.map_id==runearrow.map_():
                self.rune_active = False
                global_var.rune_stop=0
                global_var.ss=1
                global_var.shop=1
                runearrow.go_shop(0)
                runearrow.switch_13FFF0CF0(0)
                global_var.rune_check=0
                change_channel(7)
                self.red_count=0
                count=0
                return 0
            if runearrow.rune_debuff()==1:
                    for _ in range(3):
                        target=cv2bg.capture('rune_buff_template.bmp',t=0.9,y2=global_var.y2//15)
                        if len(target)>0:
                            try:
                                target=target.split('|')
                                for i in target:
                                    click(i, button='right')
                                    time.sleep(0.001)
                            except:
                                for i in target:
                                    click(i, button='right')
                                    time.sleep(0.001)
                        while True:
                            frame=cv2bg1.capture(global_var.hwnd)
                            setting = utils.multi_match(frame,setting_,threshold=0.8)
                            time.sleep(0.3)
                            if len(setting)>0:
                                break
                            else:
                                mouse_move()
                    self.rune_active = False
                    global_var.rune_stop=0
                    global_var.ss=1
                    global_var.shop=1
                    global_var.rune_check=0
                    # runearrow.go_shop(1)
                    self.red_count=0
                    runearrow.faketime_reset(0)
                    gc.collect()
                    return 0  
            elif count!=0:
                print('shop')
                while True:
                    
                    # while True:
                    #     if runearrow.lie()==0:
                    #         time.sleep(1)
                    #         break
                    #     else:
                    #         time.sleep(1)
                    
                    press("g", 3, down_time=0.2)
                    mouse_move()
                    frame=cv2bg1.capture(global_var.hwnd)
                    ok2 = utils.multi_match(frame,ok2_,threshold=0.8)
                    # time.sleep(0.05)
                    # shop_1 = utils.multi_match(frame,
                    #                             shop_,
                    #                             threshold=0.9)
                
                    # if shop_1:
                    #     shop_pos = min(shop_1, key=lambda p: p[0])
                    #     target = (
                    #         round(shop_pos[0] + global_var.window['left']),
                    #         round(shop_pos[1] + global_var.window['top'])
                    #     )
                    #     print(target)
                    #     click(target, button='left')
                    #     break
                    if len(ok2)==0:
                        break
                    elif len(ok2)>0:
                        # runearrow.go_shop(0)
                        press("enter", 1, down_time=0.5)
                        time.sleep(0.05)
                    time.sleep(1)
                
                time.sleep(5)
                target=cv2bg.capture('save.bmp',t=0.8)
                if len(target)>0:
                    click(target, button='left')
                time.sleep(0.3)
                target=cv2bg.capture('leave_shop.bmp',t=0.8)
                print(target)
                if len(target)>0:
                    click(target, button='left')
                    # break
                
        
                while True:
                    frame=cv2bg1.capture(global_var.hwnd)
                    setting = utils.multi_match(frame,setting_,threshold=0.8)
                    
                    time.sleep(0.3)
                    if len(setting)>0:
                        break
                    else:
                        mouse_move()
                count=0
            elif runearrow.rune_debuff()==0:
            # if count>0 and count%1==0:
                # while True:
                    runearrow.target()
                    time.sleep(1)
                    adjust = self.command_book['adjust']
                    adjust(*self.rune_pos).execute()
                    global_var.rune_stop=1
                    time.sleep(0.5)
                    press(self.config['Interact'], 1, down_time=1)        # Inherited from Configurable
                    print('\nSolving rune:')
                    inferences = []
                    # for _ in range(15):
                    # frame = config.capture.frame
                    #runearrow.rune_arrow_adr()
                    time.sleep(0.1)
                    solution=runearrow.arrow()
                    # solution = detection.merge_detection(model, frame)
                    # if solution:
                    #     print(', '.join(solution))
                    #     if solution in inferences:
                    #         print('Solution found, entering result')
                    print(solution)
                    time.sleep(1)
                    for arrow in solution:
                        press(arrow, 1, down_time=0.001,up_time=0.001)
                    time.sleep(0.1)
                    global_var.rune_stop=0
                    count+=1
                    
                    # if runearrow.rune_debuff()==0:
                        # move = self.command_book['move']
                        # move(*self.rune_pos).execute()
                        
                    # press("f11")
                    # self.red_count+=1
                    # count=0
                    # break
                    # time.sleep(5)
                    # while True:
                    #     time.sleep(0.3)
                    #     frame = cv2bg.capture(global_var.hwnd)
                    #     mouse_move()
                    #     leave = utils.multi_match(frame,
                    #                                     leave_shop,
                    #                                     threshold=0.7)
                    #     print(leave)
                    #     if leave:
                    #         leave_pos = min(leave, key=lambda p: p[0])
                    #         target = (
                    #             round(leave_pos[0] + global_var.window['left']),
                    #             round(leave_pos[1] + global_var.window['top'])
                    #         )

                    #         click(target, button='left')
                            
                    #         break
                    #     else:
                    #         mouse_move()
                            
                    #     time.sleep(0.05)
                    # del leave,frame,rune_buff
                    # gc.collect()
            
            
                # count+=1
        # if runearrow.rune_debuff()==1:
        #     for _ in range(3):
        #         target=cv2bg.capture('rune_buff_template.bmp',t=0.9,y2=global_var.y2//15)
        #         # frame = cv2bg.capture(global_var.hwnd)
        #         # rune_buff = utils.multi_match(frame[:frame.shape[0] // 5, :],
        #         #                                 RUNE_BUFF_TEMPLATE,
        #         #                                 threshold=0.5)
        #         # print(rune_buff)
        #         # if rune_buff:
        #         #     rune_buff_pos = min(rune_buff, key=lambda p: p[0])
        #         #     target = (
        #         #         round(rune_buff_pos[0] + global_var.window['left']),
        #         #         round(rune_buff_pos[1] + global_var.window['top'])
        #         #     )
        #         #     print(target)
        #         if len(target)>0:
        #             try:
        #                 target=target.split('|')
        #                 for i in target:
        #                     click(i, button='right')
        #                     time.sleep(0.001)
        #             except:
        #                 for i in target:
        #                     click(i, button='right')
        #                     time.sleep(0.001)
        #         while True:
        #             frame=cv2bg1.capture(global_var.hwnd)
        #             setting = utils.multi_match(frame,setting_,threshold=0.8)
        #             time.sleep(0.3)
        #             if len(setting)>0:
        #                 break
        #             else:
        #                 mouse_move()
        #     self.rune_active = False
        #     global_var.rune_stop=0
        #     global_var.ss=1
        #     global_var.shop=1
        #     global_var.rune_check=0
        #     # runearrow.go_shop(1)
        #     self.red_count=0
        #     runearrow.faketime_reset(0)
        #     gc.collect()
        #     return 0
                    # if count==9:
                    #     self.rune_active = False
                    #     global_var.shop=1
                    #     runearrow.go_shop(0)
                    #     runearrow.walk(1)
                    #     global_var.rune_check=0
                    #     global_var.rune_x=0
                    #     global_var.rune_y=0
                        
                    #     count=0
                    #     break
                    
              
                    
                        # press("`", 3, down_time=0.2)
                        # mouse_move()
                        # img = pyautogui.screenshot(region=[0,0,1920,1080])
                        # img = cv2.cvtColor(np.asarray(img), cv2.COLOR_RGB2BGR)
                        # img_np = np.array(img)
                        # frame=cv2bg.capture(global_var.hwnd)
                        # ok2 = utils.multi_match(frame,ok2_,threshold=0.8)
                        # time.sleep(0.05)
                        # if len(ok2)>0:
                        #     press("enter", 1, down_time=0.5)
                        #     time.sleep(0.05)
                        # else:
                        #     del ok2
                        #     gc.collect()
                        #     break
                
                    
                    

def change_channel(t):
    if global_var.fiola_check==0:
        
        global_var.channel=1
        global_var.shop=0
        global_var.ss=0
        global_var.stop=True
        runearrow.go_shop(0)
        time.sleep(t)
        
        while True:
            try:
                if global_var.fiola_check==0:
                    if runearrow.fire_() ==1 or runearrow.red_()>2:
                        press("f11")
                        press("=", 1, down_time=0.2)
                        time.sleep(0.5)
                        for i in range(1,randint(3,20)):
                            press("right", 1, down_time=0.0001,nd=1)
                        time.sleep(0.5)
                        press('enter',1,down_time=0.2)
                        mouse_move()
                        ok2 = cv2bg.capture('ok2.bmp')
                        time.sleep(0.05)
                        if len(ok2)>0:
                            press("enter", 1, down_time=0.5)
                        time.sleep(3)
                    elif runearrow.fire_() ==0 and runearrow.red_()==2:
                        time.sleep(3)
                        press("f11")
                        press("t", 1, down_time=0.5)
                        global_var.shop=1
                        global_var.channel=0
                        global_var.ss=1
                        global_var.stop=False
                        break
                else:
                    global_var.channel=0
                    global_var.shop=1
                    global_var.ss=1
                    runearrow.go_shop(1)
                    break
                time.sleep(0.5)
            except:
                continue
