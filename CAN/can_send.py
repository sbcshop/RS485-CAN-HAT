import os
import can

os.system('sudo ip link set can0 type can bitrate 100000')
os.system('sudo ifconfig can0 up')

bus = can.interface.Bus(channel = 'can0', bustype = 'socketcan_ctypes')# socketcan_native

message = can.Message(arbitration_id=0x124, data=[0, 1, 2, 3, 4, 5, 6, 7], extended_id=False)

bus.send(message)

os.system('sudo ifconfig can0 down')
