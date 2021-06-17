import RPi.GPIO as GPIO
import time

RoAPin = 11
RoBPin = 13

globalCounter = 0

class Wheel:
    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(RoAPin, GPIO.IN)
        GPIO.setup(RoBPin, GPIO.IN)
        self.aLastState = GPIO.LOW
        self.aState = GPIO.LOW
        self.counter = 0
    def getRotate(self):
        self.aState = GPIO.input(RoAPin)
        if self.aState != self.aLastState:
            if GPIO.input(RoBPin) != self.aState:
                self.counter += 1
            else:
                self.counter -= 1
        self.aLastState = self.aState
        return self.counter

if __name__ == '__main__':
    wheel = Wheel()
    while True:
        print(wheel.getRotate())

