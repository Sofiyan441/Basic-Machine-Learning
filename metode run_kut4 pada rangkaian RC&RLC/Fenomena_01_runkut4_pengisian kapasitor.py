import numpy as np
from printSoln import *
from run_kut4 import *
import matplotlib.pyplot as plt

# input data
r=1.0e3     # resistansi sebesar 1 kohm
e=5.0       # nilai tegangan awal 5 volt
c=1.0e-3    # kapasitansi sebesar 1 mF
# y adalah tegangan
# persamaan diferensial biasa pengisian kapasitor RC
def F(x,y):
    F = np.zeros(1)
    F[0] = (1/(r*c))*(e-y[0])
    return F

x = 0.0 # Mulai menghitung
xStop = 20.0 # Selesai menghitung
y = np.array([0.0]) # Kondisi awal (y)
h = 0.1 #Step size
freq = 1
#solusi numerik  menggunakan Runge-Kutta orde4
X,Y = integrate(F,x,y,xStop,h)

# memprint nilai solusi runge-kutta orde4
print("--- SOLUSI PDB METODE RUNGE-KUTTA ORDE 4---")
print("-----------------------------------------")
printSoln(X,Y,freq)
print("-----------------------------------------")

# memplot nilai solusi untuk runge-kutta
plt.plot(X,Y[:,0],'o')
plt.grid(True)
plt.title('Grafik Pengisian Muatan Kapasitor Rangkaian RC')
plt.xlabel('Waktu (s)'); plt.ylabel('Tegangan (Volt)')
plt.show()

input("Fress return to exit")
