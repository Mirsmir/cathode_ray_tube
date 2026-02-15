from src import typingSpeed
from pynput import keyboard
from src import serialComm
import pygame
import threading 
import time
from src.keySound import keySoundController

wpm = 0


def classify_key(key):

    if key == keyboard.Key.enter:
        return "enter_space"

    if key == keyboard.Key.backspace:
        return "backspace"

    try:
        k = key.char.lower()
    except AttributeError:
        return None   

    if k in {'[', ']', '(', ')', '{', '}', '<', '>'}:
        return "brackets"

    if k in {'a', 'o', 'u', 'e', 'i', 'y'}:
        return "vowel"

    if k in {
        'q','w','r','t','p','s','d','f','g','h','j','k','l',
        'z','x','c','v','b','n','m'
    }:
        return "const"
    
    if k in {
		'1','2','3','4','5','6','7','8','9','0'
	}:
        return "nums"

    return None


group_sounds = {
    "vowel": "vowel.wav",
    "brackets": "brackets.mp3",
    "enter_space": "enter_space.mp3",
    "const": "const.wav",
    "backspace": "backspace.mp3",
    "nums": "nums.wav"

}

def start_wpm_music_controller(
    synth_mp3,
    fastSynth_mp3,
    wpm_threshold=50,
    wpm_theshold_fast=90,
    poll_interval=0.5
):

	def audio_loop():
			pygame.mixer.init()
			current_track = None

			while typingSpeed.is_running():
				wpm = typingSpeed.get_wpm()

				if wpm < wpm_threshold:
					desired = synth_mp3
				else:
					desired = fastSynth_mp3

				if desired != current_track:
					pygame.mixer.music.stop()
					pygame.mixer.music.load(desired)
					pygame.mixer.music.play(loops=-1)
					current_track = desired

				time.sleep(poll_interval)

			pygame.mixer.music.stop()
			pygame.mixer.quit()
   
	thread = threading.Thread(target=audio_loop, daemon=True)
	thread.start()
	return thread



def poll_wpm(interval_s=1.0):
	global wpm
	while typingSpeed.is_running():
		wpm = typingSpeed.get_wpm()
		print(f"WPM (polled): {wpm:.1f}")
		time.sleep(interval_s)
		# print("what the fuck") 
		serialComm.send_wpm_signal(arduino, wpm) 	
	#will send the wpm to the arduino, and then we can parce it from there.
  

if __name__ == "__main__":
	arduino = serialComm.connect_arduino()	
	typingSpeed.start_listener()
 
	key_controller = keySoundController(
        classifier=classify_key,
        group_sounds=group_sounds
    
    )
 
	start_wpm_music_controller(
        "synth.mp3",
        "fastSynth.mp3",
        wpm_threshold=50
    )
 
	key_controller.start()
	poll_wpm(1.0)
	# every 1000mslsdef main():
    # global wpm

	

	    
        
  

        

