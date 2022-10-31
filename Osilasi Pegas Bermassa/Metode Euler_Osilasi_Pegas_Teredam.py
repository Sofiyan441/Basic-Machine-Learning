import numpy as np
from printSoln import *
from euler import *
import matplotlib.pyplot as plt

# input data
k=2.00
m=2.00
b=1.00

#persamaan diferensial biasa
def F(x,y):
    F = np.zeros(2)
    F[0] = y[1]
    F[1] = -(k/m)*y[0]-(b/m)*y[1]
    
    return F

x = 0.0 # Start of integration
xStop = 20.0 # End of integration
y = np.array([0.02,0]) #kondisi awal{y}
h = 0.1 # Step size
freq = 1
# solusi numerik menggunakan euler
X,Y = integrate(F,x,y,xStop,h)

#memprint nilai solusi numerik
print("---METODE NUMERIK PDB EULER---")
printSoln(X,Y,freq)

# memplot solusi untuk posisi
plt.subplot(2,1,1)
plt.plot(X,Y[:,0],'-')
plt.title('GRAFIK POSISI TERHADAP WAKTU')
plt.xlabel('Waktu(s)'); plt.ylabel('Posisi(m)')
plt.grid(True)

# memplot solusi untuk kecepatan
plt.subplot(2,1,2)
plt.plot(X,Y[:,1],'-')
plt.title('GRAFIK KECEPATAN TERHADAP WAKTU')
plt.xlabel('Waktu(s)'); plt.ylabel('Kecepatan(m/s)')
plt.grid(True)
plt.show()

input("Press return to exit")
