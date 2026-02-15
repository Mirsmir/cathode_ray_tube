from src import typingSpeed
from src import serialComm
import time

wpm = 0

def poll_wpm(interval_s=1.0):
	global wpm
	while typingSpeed._is_running():
		wpm = typingSpeed.get_wpm()
		print(f"WPM (polled): {wpm:.1f}")
		time.sleep(interval_s)
		serialComm.send_wmp_signal(serialComm.connect_arduino(), wpm) 
		#will send the wpm to the arduino, and then we can parce it from there.
		print("what the fuck") 
  

if __name__ == "__main__":
	typingSpeed.start_listener()
	poll_wpm(1.0)
	# every 1000mslsdef main():
    # global wpm

	

	    
        
  

        

