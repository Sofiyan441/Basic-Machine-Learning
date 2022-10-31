import matplotlib.pyplot as plt
import math
import numpy as np

t = np.arange(0,5,0.1)
y1 = np.sin(math.pi*t)
y2 = np.sin(math.pi*t+math.pi/2)
y3 = np.sin(math.pi*t-math.pi/2)

plt.subplot(3,1,1)
plt.plot(t,y1,'b--')
plt.title('Plot Data Fungsi y1')

plt.subplot(3,1,2)
plt.plot(t,y2,'g')
plt.title('Plot Data Fungsi y2')

plt.subplot(3,1,3)
plt.plot(t,y3,'r-.')
plt.title('Plot Data Fungsi y3')

plt.show()
