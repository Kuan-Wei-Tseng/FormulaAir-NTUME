
import numpy as np

x = np.array([250,255,240,243,228,264,490,225,178,252,211]);
s = np.std(x)
m = np.mean(x)
y = (x-m)/s
r = np.where(abs(y)>1)
z = np.delete(x,r)

print(z)


