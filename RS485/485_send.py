#!/usr/bin/env python3

import RPi.GPIO as GPIO
import serial
import time

RS485_ENABLE_PIN =  4 # RSE TX/RX Control Pin

GPIO.setmode(GPIO.BCM)
GPIO.setup(RS485_ENABLE_PIN,GPIO.OUT)
GPIO.output(RS485_ENABLE_PIN,GPIO.HIGH)  # Set HIGH to Transmit'''

ser  = serial.Serial("/dev/ttyS0",115200) # Open Serial Port ttyS0

MESSAGE = b"Hello from sender" # message to send

while 1:
    ser.write(MESSAGE)  # Sent message through serial port
    time.sleep(3)

ser.close()
     


