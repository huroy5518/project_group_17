import RPi.GPIO as GPIO
import time

POSPIN = 40
ENAPIN = 36
DIRPIN = 38

class Motor:
    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(POSPIN, GPIO.OUT)
        GPIO.setup(ENAPIN, GPIO.OUT)
        GPIO.setup(DIRPIN, GPIO.OUT)
    def setRotate(self, steps):
        GPIO.output(ENAPIN, GPIO.LOW)
        GPIO.output(DIRPIN, GPIO.HIGH)
        counter = 0
        try:
            while True: 
                GPIO.output(POSPIN, GPIO.HIGH)
                time.sleep(0.001)
                print("hello1")
                GPIO.output(POSPIN,GPIO.LOW)
                time.sleep(0.001)
                counter += 1
        except KeyboardInterrupt:
            print("hello")
            GPIO.cleanup()

if __name__ == '__main__':
    motor = Motor()
    motor.setRotate(1000000000)
    time.sleep(10)
    GPIO.cleanup()
