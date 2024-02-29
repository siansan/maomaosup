#-*- coding:utf-8 -*-
from google.cloud import speech
import pynput
import keyboard as kb
## 导入鼠标监听器
from pynput import keyboard
import speech_recognition
import pyperclip as pc
import threading
import time
import ctypes
import win32con
import win32api
import win32gui
from src.common import utils
from ctypes import wintypes
from random import random,randint

user32 = ctypes.WinDLL('user32', use_last_error=True)

INPUT_MOUSE = 0
INPUT_KEYBOARD = 1
INPUT_HARDWARE = 2

KEYEVENTF_EXTENDEDKEY = 0x0001
KEYEVENTF_KEYUP = 0x0002
KEYEVENTF_UNICODE = 0x0004
KEYEVENTF_SCANCODE = 0x0008

MAPVK_VK_TO_VSC = 0
wintypes.ULONG_PTR = wintypes.WPARAM
## ================================================
##              控制鼠标部分
## ================================================
# 读鼠标坐标
keyboard = pynput.keyboard.Controller()
mouse = pynput.mouse.Controller()
global n
n=''
## ================================================
##              监听鼠标部分
## ================================================
KEY_MAP = {
    'enter': 0x0D,
    'esc': 0x1B
}
wintypes.ULONG_PTR = wintypes.WPARAM
class KeyboardInput(ctypes.Structure):
    _fields_ = (('wVk', wintypes.WORD),
                ('wScan', wintypes.WORD),
                ('dwFlags', wintypes.DWORD),
                ('time', wintypes.DWORD),
                ('dwExtraInfo', wintypes.ULONG_PTR))

    def __init__(self, *args, **kwargs):
        super(KeyboardInput, self).__init__(*args, **kwargs)
        if not self.dwFlags & KEYEVENTF_UNICODE:
            self.wScan = user32.MapVirtualKeyExW(self.wVk, MAPVK_VK_TO_VSC, 0)

class MouseInput(ctypes.Structure):
    _fields_ = (('dx', wintypes.LONG),
                ('dy', wintypes.LONG),
                ('mouseData', wintypes.DWORD),
                ('dwFlags', wintypes.DWORD),
                ('time', wintypes.DWORD),
                ('dwExtraInfo', wintypes.ULONG_PTR))


class HardwareInput(ctypes.Structure):
    _fields_ = (('uMsg', wintypes.DWORD),
                ('wParamL', wintypes.WORD),
                ('wParamH', wintypes.WORD))

class Input(ctypes.Structure):
    class _Input(ctypes.Union):
        _fields_ = (('ki', KeyboardInput),
                    ('mi', MouseInput),
                    ('hi', HardwareInput))

    _anonymous_ = ('_input',)
    _fields_ = (('type', wintypes.DWORD),
                ('_input', _Input))


LPINPUT = ctypes.POINTER(Input)


def err_check(result, _, args):
    if result == 0:
        raise ctypes.WinError(ctypes.get_last_error())
    else:
        return args


user32.SendInput.errcheck = err_check
user32.SendInput.argtypes = (wintypes.UINT, LPINPUT, ctypes.c_int)
def key_down(key):
    """
    Simulates a key-down action. Can be cancelled by Bot.toggle_enabled.
    :param key:     The key to press.
    :return:        None
    """

    key = key.lower()
    if key not in KEY_MAP.keys():
        print(f"Invalid keyboard input: '{key}'.")
    else:
        x = Input(type=INPUT_KEYBOARD, ki=KeyboardInput(wVk=KEY_MAP[key]))
        user32.SendInput(1, ctypes.byref(x), ctypes.sizeof(x))


def key_up(key):
    """
    Simulates a key-up action. Cannot be cancelled by Bot.toggle_enabled.
    This is to ensure no keys are left in the 'down' state when the program pauses.
    :param key:     The key to press.
    :return:        None
    """

    key = key.lower()
    if key not in KEY_MAP.keys():
        print(f"Invalid keyboard input: '{key}'.")
    else:
        x = Input(type=INPUT_KEYBOARD, ki=KeyboardInput(wVk=KEY_MAP[key], dwFlags=KEYEVENTF_KEYUP))
        user32.SendInput(1, ctypes.byref(x), ctypes.sizeof(x))


@utils.run_if_enabled
def press():
    """
    Presses KEY N times, holding it for DOWN_TIME seconds, and releasing for UP_TIME seconds.
    :param key:         The keyboard input to press.
    :param n:           Number of times to press KEY.
    :param down_time:   Duration of down-press (in seconds).
    :param up_time:     Duration of release (in seconds).
    :return:            None
    """
    key_down("enter")
    time.sleep(0.01)
    key_up('enter')
    time.sleep(0.01)

def listen():
    global n
    client_file='C:/Users/sian/Desktop/test/new_mem_nobg/sianporject-e1d148b0e481.json'
    # credentials=service_account.Credentials.from_service_account_file(client_file)
    client=speech.SpeechClient.from_service_account_file(client_file)

    print(0)
        
    config=speech.RecognitionConfig(
    encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
    sample_rate_hertz=44100,
    language_code="zh-TW",
    )
    r=speech_recognition.Recognizer()  
    while True: 
        try:
            with speech_recognition.Microphone() as source:
            # r.adjust_for_ambient_noise(source, duration=0.01)
            # print("a")
                r.adjust_for_ambient_noise(source, duration=0.08)
                audio = r.listen(source)
            n=r.recognize_google(audio,language="zh_tw").replace(' ','')
            try:
                n=n.replace('1',"e")
            except:
                pass
            print(n)
        except:
            pass
        # with open("audio_file.wav","wb") as f:
        #     f.write(audio.get_wav_data())
        
        # with open("audio_file.wav","rb") as au:
        #     data=au.read()
        #     au=speech.RecognitionAudio(content=data)
        #     response=client.recognize(config=config,audio=au)
        #     for result in response.results:
        #         print((result.alternatives[0].transcript).replace(' ',''))
        #     n=(result.alternatives[0].transcript).replace(' ','')
        #     try:
        #         n.replace('e',"1")
        #     except:
        #         pass
        time.sleep(0.5)


# 监听鼠标移动的方法
def on_move(x, y):
    pass

# 监听鼠标点击的方法
def on_click(x,y,button, pressed):
    pass
# 监听鼠标滚轮的方法
def on_scroll(x, y, dx, dy):
    keyboard.type(n)
    key_down("enter")
    time.sleep(0.01)
    key_up('enter')
    for i in range(25):
        key_down("esc")
        time.sleep(0.01)
        key_up('esc')
def on_release():
    global n
    while True:
        if kb.is_pressed("f1"):
            keyboard.type(n)
            key_down("enter")
            time.sleep(0.01)
            key_up('enter')
            for i in range(10):
                key_down("esc")
                time.sleep(0.01)
                key_up('esc')
            time.sleep(1)
        time.sleep(0.1)

# 注册三个监听方法的监听器
def main():
    t=threading.Thread(target=listen)
    t.start()
    with pynput.mouse.Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener:
	    listener.join()
    # key_listener = threading.Thread(target=on_release)
    # key_listener.start()
# 一个鼠标监听器是一个线程。线程，所有的回调将从线程调用。从任何地方调用pynput.mouse.Listener.stop，或者调用 pynput.mouse.Listener.StopException 或从回调中返回 False 来停止监听器。

if __name__ == '__main__':
	main()