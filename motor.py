import RPi.GPIO as GPIO
import argparse
import time

parser = argparse.ArgumentParser(description="Stepper Motor")
parser.add_argument('time_delay', metavar='d', type=int, help="Delay (recommended = 0.001)")
parser.add_argument('pin1', metavar='w', type=int, help="Pin 1 (BCM numbering)")
parser.add_argument('pin2', metavar='x', type=int, help="Pin 2 (BCM numbering)")
parser.add_argument('pin3', metavar='y', type=int, help="Pin 3 (BCM numbering)")
parser.add_argument('pin4', metavar='z', type=int, help="Pin 4 (BCM numbering)")
args = parser.parse_args()
GPIO.setmode(GPIO.BCM)

class Stepper:
    def __init__(self, time_delay, pin1, pin2, pin3, pin4):
        self.time_delay = time_delay
        self.pins = [pin1, pin2, pin3, pin4]
        GPIO.setup(pin1, GPIO.OUT)
        GPIO.setup(pin2, GPIO.OUT)
        GPIO.setup(pin3, GPIO.OUT)
        GPIO.setup(pin4, GPIO.OUT)
        self.seq = [
            [1,0,0,0],
            [1,1,0,0],
            [0,1,0,0],
            [0,1,1,0],
            [0,0,1,0],
            [0,0,1,1],
            [0,0,0,1],
            [1,0,0,1]
        ]

    def turn(self, int):
        for halfstep in range(8):
            for pin in range(4):
                GPIO.output(self.pins[pin], self.seq[halfstep][pin])
            time.sleep(self.time_delay)

motor = Stepper(0.001, args.pin1,args.pin2,args.pin3,args.pin4)
while True:
    motor.turn(1)

#def get_input():
#    while True:
#        cmd = input().strip()
#        if cmd == "exit":
#            GPIO.output(args.pin1, 0)
#            GPIO.output(args.pin2, 0)
#            GPIO.output(args.pin3, 0)
#            GPIO.output(args.pin4, 0)