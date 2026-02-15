from src import typingSpeed
import time

def poll_wpm(interval_s=1.0):
	while typingSpeed._is_running():
		wpm = typingSpeed.get_wpm()
		print(f"WPM (polled): {wpm:.1f}")
		time.sleep(interval_s)
  

if __name__ == "__main__":
	# Start the typing listener in background
	typingSpeed.start_listener()
	# Poll WPM every 1000msls
	poll_wpm(1.0)


