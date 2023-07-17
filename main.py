import numpy as np
import matplotlib.pyplot as plt
data = np.loadtxt('HOM_Traces_20220814_1222_51.txt', skiprows=5)

x = data[:, 0]
y = data[:, 1]
z = data[:, 2]
a = data[:, 3]

var = [x,y,z,a]

for v in var:
    plt.plot(v, '-')
plt.show()