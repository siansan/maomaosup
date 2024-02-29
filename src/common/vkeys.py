"""A module for simulating low-level keyboard and mouse key presses."""
from random import random,randint
import time
from src.modules import global_var
from src.common import utils
import win32com.client
global dm
dm= win32com.client.Dispatch('dm.dmsoft')
dm_ret = dm.Reg('646842f3dd42de689d8e2b1ab1778cd9e204fa','0001')
hwnd=global_var.hwnd
gdi = "dx"
mouse = "dx.mouse.position.lock.api|dx.mouse.clip.lock.api|dx.mouse.input.lock.api|dx.mouse.state.api|dx.mouse.api|dx.mouse.cursor"
keyboard = "dx.keypad.input.lock.api|dx.keypad.state.api|dx.keypad.api"
public = "dx.public.active.api"
dm.BindWindowEx(hwnd,gdi,mouse,keyboard,public,0)
#################################
#           Functions           #
#################################
@utils.run_if_enabled
def key_down(key):
    """
    Simulates a key-down action. Can be cancelled by Bot.toggle_enabled.
    :param key:     The key to press.
    :return:        None
    """

    dm.KeyDownChar(key)


def key_up(key):
    """
    Simulates a key-up action. Cannot be cancelled by Bot.toggle_enabled.
    This is to ensure no keys are left in the 'down' state when the program pauses.
    :param key:     The key to press.
    :return:        None
    """

    dm.KeyUpChar(key)


@utils.run_if_enabled
def press(key, n=1, down_time=0.05, up_time=0.05,nd=None):
    """
    Presses KEY N times, holding it for DOWN_TIME seconds, and releasing for UP_TIME seconds.
    :param key:         The keyboard input to press.
    :param n:           Number of times to press KEY.
    :param down_time:   Duration of down-press (in seconds).
    :param up_time:     Duration of release (in seconds).
    :return:            None
    """
    if nd==None:
        for _ in range(n):
            key_down(key)
            time.sleep(down_time * (0.8 + 0.4 * random()))
            key_up(key)
            time.sleep(up_time * (0.8 + 0.4 * random()))
    else:
        for _ in range(n):
            key_down(key)
            time.sleep(0.0015)
            key_up(key)
            time.sleep(0.00001)

def up_jump_press(key, n=1, down_time=0.05, up_time=0.005):
    """
    Presses KEY N times, holding it for DOWN_TIME seconds, and releasing for UP_TIME seconds.
    :param key:         The keyboard input to press.
    :param n:           Number of times to press KEY.
    :param down_time:   Duration of down-press (in seconds).
    :param up_time:     Duration of release (in seconds).
    :return:            None
    """
    for _ in range(n):
        key_down(key)
        time.sleep(down_time)
        key_up(key)
        time.sleep(up_time)

@utils.run_if_enabled
def click(position, button='left'):
    """
    Simulate a mouse click with BUTTON at POSITION.
    :param position:    The (x, y) position at which to click.
    :param button:      Either the left or right mouse button.
    :return:            None
    """
    try:
        position=position.split("|")[0].split(',')
    except:
        pass
    print(position)
    if button not in ['left', 'right']:
        print(f"'{button}' is not a valid mouse button.")
    else:
        if button == 'left':
            dm.MoveTo(int(position[1]),int(position[2]))
            dm.LeftClick()
        else:
            dm.MoveTo(int(position[1]),int(position[2]))
            dm.RightClick()

def mouse_move():
    p={"x":0,"y":0}
    pos = dm.GetCursorPos()
    p['x']=pos[0]
    p['y']=pos[1]
    dm.MoveTo(p['x']+randint(-100,100),p['y']+randint(-100,100))

