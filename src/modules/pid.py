import win32gui
import win32process
import psutil
import ctypes
from src.modules import global_var
EnumWindows = ctypes.windll.user32.EnumWindows
EnumWindowsProc = ctypes.WINFUNCTYPE(ctypes.c_bool, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))
GetWindowText = ctypes.windll.user32.GetWindowTextW
GetWindowTextLength = ctypes.windll.user32.GetWindowTextLengthW
IsWindowVisible = ctypes.windll.user32.IsWindowVisible

def getProcessIDByName():
    qobuz_pids = []
    process_name = "MapleStory.exe"

    for proc in psutil.process_iter():
        if process_name in proc.name():
            qobuz_pids.append(proc.pid)

    return qobuz_pids

def get_hwnds_for_pid(pid):
    def callback(hwnd, hwnds):
        #if win32gui.IsWindowVisible(hwnd) and win32gui.IsWindowEnabled(hwnd):
        _, found_pid = win32process.GetWindowThreadProcessId(hwnd)

        if found_pid == pid:
            hwnds.append(hwnd)
        return True
    hwnds = []
    win32gui.EnumWindows(callback, hwnds)
    return hwnds 

def getWindowTitleByHandle(hwnd):
    length = GetWindowTextLength(hwnd)
    buff = ctypes.create_unicode_buffer(length + 1)
    GetWindowText(hwnd, buff, length + 1)
    return buff.value

def getQobuzHandle():
    pids = getProcessIDByName()

    for i in pids:
        hwnds = get_hwnds_for_pid(i)
        for hwnd in hwnds:
            if IsWindowVisible(hwnd):
                return hwnd


def start():
    qobuz_handle = getQobuzHandle()
    global_var.var()
    global_var.hwnd=qobuz_handle
    print(global_var.hwnd)

def clean_start():
    qobuz_handle = getQobuzHandle()
    global_var.hwnd=qobuz_handle