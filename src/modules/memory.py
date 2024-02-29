from pympler import muppy, summary
import time
import threading
import gc
def test():
    while True:
        all_objects = muppy.get_objects()
        sum1 = summary.summarize(all_objects)
        summary.print_(sum1)
        time.sleep(10)
def start():
    sound_thread = threading.Thread(target=test)
    sound_thread.daemon = True
    sound_thread.start()