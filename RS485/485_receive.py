#!/usr/bin/env python3

import RPi.GPIO as GPIO
import serial

RS485_ENABLE_PIN =  4 # RSE TX/RX Control Pin

GPIO.setmode(GPIO.BCM)
GPIO.setup(RS485_ENABLE_PIN,GPIO.OUT)
GPIO.output(RS485_ENABLE_PIN,GPIO.LOW) # Set LOW to Receive'''

ser = serial.Serial("/dev/ttyS0",115200,timeout=1)  # Open Serial Port ttyS0

while 1:
    #ser.write(b'hii')
    str = ser.readall()  # Read data Received on Serial Port
    if str:             
        print (str)      # Print received data ob terminal/shell
