import serial
import time

def connect_arduino(port='COM7', baudrate=9600): #p sure its com3???
    arduino = serial.Serial(port,baudrate,timeout=1)
    time.sleep(2)
    return arduino



