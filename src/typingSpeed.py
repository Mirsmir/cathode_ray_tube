import time
from pynput import keyboard
import threading

start_time = None
keystrokes = 0
_current_wpm = 0.0
_lock = threading.Lock()
_listener = None
_running = True

def _update_wpm():
    global _current_wpm
    with _lock:
        if start_time is None:
            _current_wpm = 0.0
            return
        elapsed = time.time() - start_time
        if elapsed <= 0:
            _current_wpm = 0.0
            return
        minutes = elapsed / 60.0
        _current_wpm = (keystrokes / 5.0) / minutes

def on_press(key):
    global start_time, keystrokes
    _update_wpm()
    if start_time is None:
        start_time = time.time()

    try:
        if key.char is not None:
            with _lock:
                keystrokes += 1
    except AttributeError:
        pass

    # elapsed = time.time() - start_time
    # if elapsed >= 1:
    #     minutes = elapsed / 60
    #     wpm = (keystrokes / 5) / minutes
    #     print(f"\rWPM: {wpm:.1f}", end="")

def on_release(key):
   
    if key == keyboard.Key.esc:
        _running = False
        return False

def start_listener(print_banner=True):
    """start keyboard listener in bg thread.

    call get_wpm() to read current WPM from prev thread.
    """
    
    #tells the function thaat were looking at the global variable _listener and _running not the local ones
    global _listener, _running
    if print_banner:
        print("typing speed — listener started")
        print("press esc to stop listener \n")

    if _listener is None:
        _listener = keyboard.Listener(on_press=on_press, on_release=on_release)
        _listener.start()
    return _listener

def get_wpm():
    """most recent wpm"""
    with _lock:
        return _current_wpm

def stop_listener():
    global _listener
    if _listener is not None:
        _listener.stop()
        _listener = None

def _is_running():
    return _running;