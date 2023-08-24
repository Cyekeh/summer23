import numpy as np
import matplotlib.pyplot as plt
data = np.loadtxt('HOM_Traces_20220814_1222_51.txt', skiprows=5)

ch0 = data[:, 0]
ch1 = data[:, 1]
ch2 = data[:, 2]
ch3 = data[:, 3]

fig, ax = plt.subplots(1,2)
var = [ch0,ch1,ch2,ch3]

for i, chx in enumerate(var):
    arr = np.array(chx)
    print('Max:', np.amax(arr))
    print('Min:', np.amin(arr))
    print('Average:', np.average(chx))
    ax[0].plot(i, np.amax(arr), '.')
    ax[1].plot(i, np.amin(arr), '.')

ax[0].set_xlabel("Channel")
ax[0].set_ylabel("Scope Traces")
ax[0].set_title('Maximum')
ax[1].set_xlabel("Channel")
ax[1].set_ylabel("Scope Traces")
ax[1].set_title('Minimum')
plt.show()

