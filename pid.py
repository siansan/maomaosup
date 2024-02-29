from ctypes import wintypes
import ctypes
user32 = ctypes.windll.user32
user32.SetProcessDPIAware()
handle = user32.FindWindowW(None, 'a.jpg - 小畫家')
print(handle)