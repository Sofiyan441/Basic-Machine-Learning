import matplotlib.pyplot as plt
import numpy as np

data = np.loadtxt('kuadrat.txt')

plt.plot(data[:,0], data[:,1])
plt.title('Data"kuadrat.txt"')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
