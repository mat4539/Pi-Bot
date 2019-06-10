import subprocess
import time
p = subprocess.Popen(['python', 'motor.py', '0', '14', '15', '18', '23'])
p1 = subprocess.Popen(['python', 'motor.py', '0', '17', '4', '3', '2']) # 2 3 4 17
time.sleep(14)
p.kill()
p1.kill()
