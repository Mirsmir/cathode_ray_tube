import serial
import time

def connect_arduino(port='COM7', baudrate=9600): #p sure its com3???
    arduino = serial.Serial(port,baudrate,timeout=1)
    time.sleep(2)
    return arduino

def send_sunset_signal(arduino):
    arduino.write(b'E') #send E char to arduino 
    
def send_sunrise_signal(arduino):
    arduino.write(b'M') #send M chat to arduino
    
def send_rain_signal(arduino):
    arduino.write(b'R') #send R char to arduino
    
def send_daylight_signal(arduino):
    arduino.write(b'D') 
    
def send_off_signal(arduino):
    arduino.write(b'O')
