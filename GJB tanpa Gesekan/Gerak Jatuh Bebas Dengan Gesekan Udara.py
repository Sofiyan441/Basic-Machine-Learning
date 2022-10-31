import numpy as np
from printSoln import *
from euler import *
import matplotlib.pyplot as plt

# input data
g=9.8
b=7.0
m=70.0

#persamaan diferensial biasa
def F(x,y):
    F = np.zeros(1)
    F[0] = g - (b/m)*y[0]
    return F
x = 0.0 # Start of integration
xStop = 20.0 # End of integration
y = np.array([0.0]) #Initial values of {y}
h = 0.1 # Step size
freq = 1
# solusi numerik menggunakan Euler
X,Y = integrate(F,x,y,xStop,h)

# solusi eksak
Yexact = (g*m/b)*(1-np.exp(-(b/m)*X));

#memprint nilai solusi euler dan eksak
print("---SOLUSI PDB MENGGUNAKAN METODE EULER---")
print("-----------------------------------------")
printSoln(X,Y,freq)
print("-----------------------------------------")

# memplot nilai solusi euler dan eksak
plt.plot(X,Y[:,0],'o',X,Yexact,'-')
plt.grid(True)
plt.title(' Grafik Gerak Jatuh dengan Gesekan Udara')
plt.xlabel('waktu,t (s)'); plt.ylabel('Kecepatan,v(m/s)')
plt.legend(('Euler','Exact'),loc=0)
plt.show()

input("Press return to exit")
