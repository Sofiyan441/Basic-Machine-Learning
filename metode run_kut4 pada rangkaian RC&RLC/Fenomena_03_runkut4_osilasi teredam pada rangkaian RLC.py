import numpy as np
from printSoln import *
from run_kut4 import *
import matplotlib.pyplot as plt

# input data
r=1     # resistansi sebesar 1 kohm
c=1.0e-3    # kapasitansi sebesar 1 mF
l=4.0e-3    # induktansi sebesar 4 mH
# y[1] adalah perubahan tegangan terhadap waktu
# y[0] adalah tegangan

# persamaan diferensial biasa sistem osilasi teredam RLC
def F(x,y):
    F = np.zeros(2)
    F[0] = y[1]
    F[1] = -(r/l)*y[1]-(1/(l*c))*y[0]
    return F

x = 0.0 # Mulai menghitung
xStop = 0.05 # Selesai menghitung
y = np.array([5.0,0.0]) # Kondisi awal (y) tegangan kapasitor 5V
h = 0.001 #Step size
freq = 1
#solusi numerik  menggunakan Runge-Kutta orde4
X,Y = integrate(F,x,y,xStop,h)

# memprint nilai solusi runge-kutta orde4
print("--- SOLUSI PDB METODE RUNGE-KUTTA ORDE 4---")
print("-----------------------------------------")
printSoln(X,Y,freq)
print("-----------------------------------------")

# memplot nilai solusi untuk runge-kutta
plt.plot(X,Y[:,0],'o-')
plt.grid(True)
plt.title('Grafik Sistem Osilasi Teredam Rangkaian RLC')
plt.xlabel('Waktu (s)'); plt.ylabel('Tegangan (Volt)')

plt.show()
