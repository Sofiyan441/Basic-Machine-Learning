from sklearn import svm

#Database : Gerbang logika AND
#x = Data, y = Target
x = [[0,0], [0,1], [1,0], [1,1]]
y = [0, 0, 0 , 1]

#Trainning dan classify
clf = svm.SVC()
clf.fit(x,y)

#Prediksi
print ("Logika AND Metode Supprort Vektor Machine (SVM)")
print ("Logika = Prediksi")
print ("0 0 = ", clf.predict([[0,0]]))
print ("0 1 = ", clf.predict([[0,1]]))
print ("1 0 = ", clf.predict([[1,0]]))
print ("1 1 = ", clf.predict([[1,1]]))
