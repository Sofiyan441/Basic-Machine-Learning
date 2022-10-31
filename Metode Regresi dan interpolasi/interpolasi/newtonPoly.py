##module newtonPoly
''' p = evalPoly(a,xData,x).
    Menghitung Polinomial Newton p saat x. Koefisien
    vektor 'a' dapat dihitung dengan fungsi 'coeffts'.

    a = coeffts(xData,yData).
    Menghitung koefisien polinom Newton.
'''
def evalPoly(a,xData,x):
    n = len(xData) - 1 #Degree of polynomial
    p = a[n]
    for k in range(1,n+1):
        p = a[n-k] + (x-xData[n-k])*p
    return p

def coeffts(xData,yData):
    m = len(xData) #Number of data points
    a = yData.copy()
    for k in range(1,m):
        a[k:m] = (a[k:m] - a[k-1])/(xData[k:m] - xData[k-1])
    return a
