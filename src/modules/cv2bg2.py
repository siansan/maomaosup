from PIL import ImageGrab
import numpy as np
import cv2
import win32gui
def capture(hwnd):
    left, top, right, bot = win32gui.GetWindowRect(hwnd)
    img = ImageGrab.grab(bbox = (left, top, right, bot))
    img_np = np.array(img)
    img_np = cv2.cvtColor(img_np, cv2.COLOR_RGB2BGR)
    return img_np
def minimap_c(hwnd):
    left, top, right, bot = win32gui.GetWindowRect(hwnd)
    img = ImageGrab.grab(bbox = (left, top, right//3, bot//2))
    img_np = np.array(img)
    img_np = cv2.cvtColor(img_np, cv2.COLOR_RGB2BGR)
    return img_np
def rune_c(hwnd):
    left, top, right, bot = win32gui.GetWindowRect(hwnd)
    img = ImageGrab.grab(bbox = (left, top, right, bot//6))
    img_np = np.array(img)
    img_np = cv2.cvtColor(img_np, cv2.COLOR_RGB2BGR)
    return img_np