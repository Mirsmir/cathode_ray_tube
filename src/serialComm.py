import serial
import time

def connect_arduino(port='COM3', baudrate=9600): #p sure its com3???
    arduino = serial.Serial(port,baudrate,timeout=1)
    time.sleep(2)
    return arduino

def send_wpm_signal(arduino, wpm):
    msg = f"WPM:{wpm:.1f}\n"
    arduino.write(msg.encode('utf-8'))


