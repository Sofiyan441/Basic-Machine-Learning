import matplotlib.pyplot as plt
X, Y = [], []
for line in open('kuadrat.txt','r'):
    nilai = [float(s) for s in line.split()]
    X.append(nilai[0]) # nilai sumbu x
    Y.append(nilai[1]) # nilai sumbu y
plt.plot(X, Y) 
plt.title('Data"kuadrat.txt"')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
