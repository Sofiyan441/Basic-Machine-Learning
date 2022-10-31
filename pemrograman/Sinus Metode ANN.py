from sklearn.neural_network import MLPRegressor
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Database 
FileDB = 'datasinus.txt'
Database = pd.read_csv(FileDB, sep=",", header=0)
print ("---------------------")
print (Database)
#x = data, y= target
x = Database[[u'Feature']]
y = Database.Target
#fit model regresi neural network
regr = MLPRegressor(solver='lbfgs', alpha=1e-2,
                    hidden_layer_sizes=(200, 200),
                    random_state=1, max_iter=100000,
                    warm_start=True)
regr.fit(x, y)
#menampilkan data prediksi
xx = np.arange(1, 21, 1)
n = len (xx)
print ("xx(i)   neural network")
for i in range (n):
    y_neural = regr.predict([[xx[i]]])
    print ('{:.2f}'.format(xx[i]), y_neural)
#prediksi
y_neural2 = regr.predict(x)
plt.figure()
plt.plot(x, y_neural2, color = 'red')
plt.scatter(x,y, color ='blue')
plt.title ('Prediksi Data Menggunakan ANN')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(['neural networks', 'data'],loc=2)
plt.show()

    
