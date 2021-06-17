import smbus
import time
from math import *

deviceAddress = 0x69

bus = smbus.SMBus(1); 

x_byte_L = 0x69
x_byte_R = 0x70
y_byte_L = 0x87
y_byte_R = 0x88
SW_byte = 0x86

class IIC():
    def __init__(self, ADDRESS):
        self.ADDRESS = ADDRESS
    def write(self, adr, value):
        bus.write_byte_data(self.ADDRESS, adr, value)
    def read(self, adr):
        return bus.read_byte_data(self.ADDRESS, adr)
        
class STM():
    def __init__(self, ADDRESS):
        self.ADDRESS = ADDRESS
        self.norm_x = 0
        self.norm_y = 0
    def write(self, adr, value):
        bus.write_byte_data(self.ADDRESS, adr, value)
    def read(self, adr):
        return bus.read_byte_data(self.ADDRESS, adr)
    def getRawX(self):
        return self.read(x_byte_L) << 8 | self.read(x_byte_R)
    def getRawY(self):
        return self.read(y_byte_L) << 8 | self.read(y_byte_R)
    def getSW(self):
        return self.read(SW_byte)

    def getX(self):
        return (self.getRawX() - self.norm_x)
    def getY(self):
        return (self.getRawY() - self.norm_y)
    def calibrate(self):
        for i in range(1000):
            self.norm_x += self.getRawX()
            self.norm_y += self.getRawY()
        self.norm_x = self.norm_x / 1000
        self.norm_y = self.norm_y / 1000

if __name__ == '__main__':
    tmp = STM(deviceAddress)
    while True:
        val_x, val_y, val_SW = tmp.getX(), tmp.getY(), tmp.getSW() 
        print('x:%d, y:%d, sw:%d\n' % (val_x, val_y, val_SW))
        time.sleep(0.1) 
