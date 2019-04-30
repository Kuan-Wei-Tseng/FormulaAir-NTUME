# Configuration file:
# Resolution of the Image:
import numpy as np

RES = [640,480]
# Number of slices in the Image:
C1 = 10
C2 = 5
NUMofCUT = C1+C2
# Gives an array of the slices' x coordinate.
CUTHEIGHT = np.linspace(RES[1]-10,RES[1]/2,num = C1).astype(int)
CUTHEIGHT = np.append(CUTHEIGHT,np.linspace(RES[1]/2,20,num = C2).astype(int))
# print(CUTHEIGHT)
# Percentage of tolerance when detecting unexpected points:
tol = 0.3 * RES[0]
CENTER = int(RES[0]/2)
# Servo Motor settings
SERVO_PIN = 4
PWM_FREQ = 50
DEVNAME = '/dev/ttyACM1'
cmdlist = [0,1]