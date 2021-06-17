import socket
import time
from i2c_connect import STM
from wheel import Wheel
import threading

HOST = '192.168.199.2'
PORT1 = 62221
TARG = '192.168.199.1'
PORT2 = 62222

stm = STM(0x69)
wheel = Wheel()
def transfer_wheel():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        while True:
            rotate = wheel.getRotate()
            s.sendto(rotate.to_bytes(2, 'little', signed = True), (TARG, PORT1))

def transfer_pad():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        while True:
            X = int(stm.getX())
            Y = int(stm.getY())
            s.sendto(X.to_bytes(2, 'little', signed = False), (TARG, PORT2))
            s.sendto(Y.to_bytes(2, 'little', signed = False), (TARG, PORT2))

threads = []
if __name__ == '__main__':
    
    threading.Thread(target = transfer_wheel).start()
    threading.Thread(target = transfer_pad).start()
    
