from sklearn.neighbors import NearestCentroid
import numpy as np
import pandas as pd

FileDB = 'logikaand.txt'
Database = pd.read_csv(FileDB, sep=',', header=0)
print(Database)

x = Database[[u'Feature1', u'Feature2']]
y = Database.Target

clf = NearestCentroid()
clf.fit(x, y)

#Prediksi
print ("Logika AND Metode Metode K. Nearest Neighbors (KNN)")
print ("Logika = Prediksi")
print ("0 0 = ", clf.predict([[0,0]]))
print ("0 1 = ", clf.predict([[0,1]]))
print ("1 0 = ", clf.predict([[1,0]]))
print ("1 1 = ", clf.predict([[1,1]]))
