import os
import can

os.system('sudo ip link set can0 type can bitrate 100000')
os.system('sudo ifconfig can0 up') # Enable can0 

bus = can.interface.Bus(channel = 'can0', bustype = 'socketcan_ctypes')# socketcan_native


while 1:
    message = bus.recv(10.0)
    print (message)
    
    if msg is None:
        print('Timeout occurred, no message received.')

    os.system('sudo ifconfig can0 down')  #Disable can0