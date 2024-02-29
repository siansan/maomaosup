from src.modules import cv2bg
from src.common.vkeys import press, click
from src.common import config, utils
import cv2
import time
import win32con
import win32api
import win32gui
import time
import cv2
import threading
import ctypes
import mss
import mss.windows
import numpy as np
from src.common import config, utils
from ctypes import wintypes
import pyautogui
from src.modules import global_var
import re
from src.modules import runearrow
import random
import gc
from src.common.vkeys import press, click,mouse_move,key_down,key_up
user32 = ctypes.windll.user32
user32.SetProcessDPIAware()
import pyautogui
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
window = {
            'left': 0,
            'top': 0,
            'width': 1920,
            'height': 1080
        }
# The player's symbol on the minimap
PLAYER_TEMPLATE = cv2.imread('assets/player_template.png', 0)
PT_HEIGHT, PT_WIDTH = PLAYER_TEMPLATE.shape
x = cv2.imread('assets/leave_shop.jpg', 0)
handle = 263604
rect = wintypes.RECT()
user32.GetWindowRect(handle, ctypes.pointer(rect))
rect = (rect.left, rect.top, rect.right, rect.bottom)
rect = tuple(max(0, x) for x in rect)
window['left'] = rect[0]
window['top'] = rect[1]
window['width'] = max(rect[2] - rect[0], MMT_WIDTH)
window['height'] = max(rect[3] - rect[1], MMT_HEIGHT)
frame = cv2bg.capture(263604)
cv2.imshow('',frame)
cv2.waitKey()
rune_buff = utils.multi_match(frame,
                                x,
                                threshold=0.7)
print(rune_buff)
if rune_buff:
    rune_buff_pos = min(rune_buff, key=lambda p: p[0])
    target = (
        round(rune_buff_pos[0] + window['left']),
        round(rune_buff_pos[1] + window['top'])
    )
    print(target)
    down_event = win32con.MOUSEEVENTF_RIGHTDOWN
    up_event = win32con.MOUSEEVENTF_RIGHTUP
    position=target
    win32api.SetCursorPos(position)
    win32api.mouse_event(down_event, position[0], position[1], 0, 0)
    win32api.mouse_event(up_event, position[0], position[1], 0, 0)