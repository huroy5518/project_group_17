import socket
import time
import threading

HOST = '192.168.199.2'
PORT1 = 62221
TARG = '192.168.199.1'
PORT2 = 62222

def transfer_wheel():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        while True:
            rotate = 1
            s.sendto(rotate.to_bytes(2, 'little', signed = True), (TARG, PORT1))

def transfer_pad():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        while True:
            X = 3
            Y = 4
            s.sendto(X.to_bytes(2, 'little', signed = False), (TARG, PORT2))
            s.sendto(Y.to_bytes(2, 'little', signed = False), (TARG, PORT2))

threads = []
if __name__ == '__main__':
    
    threading.Thread(target = transfer_pad).start()
    threading.Thread(target = transfer_wheel).start()
    
