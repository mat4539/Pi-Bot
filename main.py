import subprocess
import time
import matping
class Motor:
    def __init__(self, pin1, pin2, pin3, pin4):
        self.pin1 = pin1
        self.pin2 = pin2
        self.pin3 = pin3
        self.pin4 = pin4
        self.pins = [self.pin1, self.pin2, self.pin3, self.pin4]
        self.running = False
        self.process = None

    def create_process(self):
        self.process = subprocess.Popen(['python', 'motor.py', '0', str(self.pins[0]), str(self.pins[1]), str(self.pins[2]), str(self.pins[3])])
        self.running = True
    
    def kill_process(self):
        self.process.kill()
        self.running = False

    def turn(self, inverted=False):
        if self.running:
            self.process.kill()

        if inverted:
            turnprocess = subprocess.Popen(['python', 'motor.py', '0', str(self.pins[3]),str(self.pins[2]),str(self.pins[1]),str(self.pins[0])])
        else:
            turnprocess = subprocess.Popen(['python', 'motor.py', '0', str(self.pins[0]),str(self.pins[1]),str(self.pins[2]),str(self.pins[3])])
        time.sleep(5)
        turnprocess.kill()
        self.create_process()
        return

motor1 = Motor(21,20,16,12)
motor1.create_process()
motor2 = Motor(2,3,4,17)
motor2.create_process()

while True:
    dist = matping.read_dist()
    print(dist)
    if dist < 10:
        if motor1.running:
            motor1.turn(inverted=True)
        if motor2.running:
            motor2.turn(inverted=False)
    else:
        if not motor1.running:
            motor1.create_process()
        if not motor2.running:
            motor2.create_process()