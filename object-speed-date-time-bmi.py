# Create a program that determines how quickly an object is traveling when it hits the
# ground. The user will enter the height from which the object is dropped in meters (m).
# Because the object is dropped its initial speed is 0 m/s. Assume that the acceleration
# due to gravity is 9.8 m/s2. You can use the formula vf = sqrt(v**2_i + 2*a*d) to compute the
# final speed, vf , when the initial speed, vi , acceleration, a, and distance, d, are known.

import math

def all_Data(h: float):
    i = 0.0
    a = 9.8
    v = math.sqrt(i**2 + (2 * a * h))
    print(v)
    return v
all_Data(100)

from time import asctime

k = asctime()
print(k)

w = 95.0
h = 1.78
t = w / (h * h)
print(t)
