# Configuration file:
# Resolution of the Image:
import numpy as np

RES = [640,480]
# Number of slices in the Image:
NUMofCUT = 10
# Gives an array of the slices' x coordinate.
CUTHEIGHT = np.linspace(RES[1]-10,20,num = NUMofCUT).astype(int)
# Percentage of tolerance when detecting unexpected points:
tol = 0.3 * RES[0]
CENTER = int(RES[0]/2)
# Servo Motor settings
SERVO_PIN = 27
PWM_FREQ = 50
DEVNAME = '/dev/ttyUSB0'
cmdlist = [0,1]