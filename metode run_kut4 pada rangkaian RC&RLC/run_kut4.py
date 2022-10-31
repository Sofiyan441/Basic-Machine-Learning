## module run_kut4
''' X,Y = integrate(F,x,y,xStop,h).
    menggunakan metode Runge-Kutta Orde-4 untuk mencari solusi
    persamaan diferensial biasa {y}' = {F(x,{y})}, dimana
    {y} = {y[0],y[1],...y[n-1]}.
    x,y   = Kondisi awal
    xStop = nilai akhir x
    h     = increment (interval) x yang digunakan
    F     = Fungsi yang ingin dicari solusinya
            array F(x,y) = {y'[0],y'[1],...y'[n-1]}.
'''
import numpy as np
def integrate(F,x,y,xStop,h):

    def run_kut4(F,x,y,h):
        K1 = h*F(x,y)
        K2 = h*F(x + h/2.0, y + K1/2.0)
        K3 = h*F(x + h/2.0, y + K2/2.0)
        K4 = h*F(x + h, y + K3)
        return (K1 + 2.0*K2 + 2.0*K3 + K4)/6.0
    X = []
    Y = []
    X.append(x)
    Y.append(y)
    while x < xStop:
        h = min(h,xStop - x)
        y = y + run_kut4(F,x,y,h)
        x = x + h
        X.append(x)
        Y.append(y)
    return np.array(X),np.array(Y)
