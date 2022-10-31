import numpy as np
from gaussElimin import*

a = np.array([[2.0, 6.0, 12.0, -8.0],
              [1, -1.0, 0.0, 0.0],
              [0.0, 1.0, -1.0, 3.0],
              [0.0, 0.0, -8.0, 10.0]])
b = np.array([0.0, -5.0, 0.0, -10.0])

aOrig = a.copy()
bOrig = b.copy()
x = gaussElimin(a,b)
det = np.prod(np.diagonal(a))
print('x=\n',x)
print('\ndet =',det)
print('\nCheck: A*x =\n',np.dot(aOrig,x))
input("\nPress return to exit")
