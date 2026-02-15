import time
from pynput import keyboard

start_time = None
keystrokes = 0

def on_press(key):
    global start_time, keystrokes

    if start_time is None:
        start_time = time.time()

    try:
        if key.char is not None:
            keystrokes += 1
    except AttributeError:
        pass

    elapsed = time.time() - start_time
    if elapsed >= 1:
        minutes = elapsed / 60
        wpm = (keystrokes / 5) / minutes
        print(f"\rWPM: {wpm:.1f}", end="")

def on_release(key):
    if key == keyboard.Key.esc:
        print("\nStopped.")
        return False

print("tyoing seep")
print("can start type now...")
print("Press esc to ESCAPE.\n")

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join() 