#Dari Library sklearn umpoer svm dan ann
from sklearn.svm import SVR
from sklearn.neural_network import MLPRegressor
import numpy as np
import matplotlib.pyplot as plt

#Database
#x = Data, y = Target
x = [[3], [6], [9]]
y = [39, 96, 171]

#Fit model regresi Support Vector Regression (SVR)
svr_rbf = SVR(kernel='rbf', C=100, gamma=0.1, epsilon=.1)
svr_rbf.fit(x, y)
svr_poly = SVR (kernel='poly', C=100, gamma='auto', degree=3,
                epsilon=.1, coef0=1)
svr_poly.fit(x, y)

#Fit model regresi neural network
reg_ann = MLPRegressor(solver='lbfgs', alpha=1e-2,
                    hidden_layer_sizes=(10,5),
                    random_state=1, max_iter=1000,
                    warm_start=True)
reg_ann.fit(x,y)
#menampilkan data prediksi
xx = np.arange(0, 10, 1)
n = len (xx)
yExcat = np.zeros((n,2))

print ("xx(i)   y_exact     y_svmrbf     y_svmpoly")
for i in range (n):
    yExact = (10.0*xx[i])+(0.5*2*xx[i]**2)
    rbf = svr_rbf.predict([[xx[i]]])
    poly = svr_poly.predict([[xx[i]]])
    y_nn = reg_ann.predict([[xx[i]]])
    print ('(:3.2f) (:9.5f)'.format(xx[i], yExact), rbf, poly, y_nn)
#plot data
rbf2   = svr_rbf.predict(x)
y_ann2 = reg_ann.predict(x)

plt.figure()
plt.plot(x, rbf2, 'r.')
plt.plot(x, y_ann2,'g-.')
plt.scatter(x,y, color = 'blue')
plt. title ('Prediksi Data Menggunakan SVM dan ANN')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(['SVM', 'ANN', 'data'], loc=2)
plt.show()
