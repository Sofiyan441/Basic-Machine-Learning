## module polyFit
''' c = polyFit(xData,yData,m).
    Menentukan nilai koefisien polynomial
    p(x) = c[0] + c[1]x + c[2]x^2 +...+ c[m]x^m
    yang memfitting data dengan metode least squares.

    sigma = stdDev(c,xDara,yData).
    Menghitung std. deviasi antara p(x) dan data.
'''

from numpy import zeros
from math import sqrt
from gaussPivot import*

def polyFit(xData,yData,m):
    a = zeros((m+1,m+1))
    b = zeros((m+1))
    s = zeros((2*m+1))
    for i in range(len(xData)):
        temp = yData[i]
        for j in range(m+1):
            b[j] = b[j] + temp
            temp = temp*xData[i]
        temp = 1.0
        for j in range(2*m+1):
            s[j] = s[j] + temp
            temp = temp*xData[i]
    for i in range(m+1):
        for j in range(m+1):
            a[i,j] = s[i+j]
    return gaussPivot(a,b)

def stdDev(c,xData,yData):

    def evalPoly(c,x):
        m = len(c) - 1
        p = c[m]
        for j in range(m):
            p = p*x + c[m-j-1]
        return p

    n = len(xData) - 1
    m = len(c) - 1
    sigma = 0.0
    for i in range(n+1):
        p = evalPoly(c,xData[i])
        sigma = sigma + (yData[i] - p)**2
    sigma = sqrt(sigma/(n - m))
    return sigma
