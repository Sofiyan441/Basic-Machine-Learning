from sklearn.neural_network import MLPClassifier
import pandas as pd

FileDB = 'logikaand.txt'
Database = pd.read_csv(FileDB, sep=',', header=0)
print(Database)

x = Database[[u'Feature1', u'Feature2']]
y = Database.Target

clf = MLPClassifier(solver='lbfgs', alpha=1e-2,
                    hidden_layer_sizes=(10,5),
                    random_state=1, max_iter=1000,
                    warm_start=True)
clf.fit(x, y)

#Prediksi
print ("Logika AND Metode Metode Artificial Neural Network (ANN)")
print ("Logika = Prediksi")
print ("0 0 = ", clf.predict([[0,0]]))
print ("0 1 = ", clf.predict([[0,1]]))
print ("1 0 = ", clf.predict([[1,0]]))
print ("1 1 = ", clf.predict([[1,1]]))
