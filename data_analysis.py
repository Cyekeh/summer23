import numpy as np
import matplotlib.pyplot as plt
data = np.loadtxt('HOM_Traces_20220814_1222_51.txt', skiprows=5)

x = data[:, 0]
y = data[:, 1]
z = data[:, 2]
a = data[:, 3]

var = [x,y,z,a]

for v in var:
    b = np.amax(v)
    print('Max:', b)
    print('Min:', np.amin(v))
    print('Average:', np.average(v))
    plt.plot(b, '.')
plt.xlabel("Time")
plt.ylabel("Scope Traces")
plt.title("Maximum")
plt.show()

for v in var:
    c = np.amin(v)
    plt.plot(c, '.')
plt.xlabel("Time")
plt.ylabel("Scope Traces")
plt.title("Minimum")
plt.show()
