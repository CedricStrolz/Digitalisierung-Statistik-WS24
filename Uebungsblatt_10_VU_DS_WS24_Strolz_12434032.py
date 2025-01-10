import numpy as np          #importieren der Numpy Library --> hier nur einmal für alle Aufgaben

#Aufgabe 1
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y = np.array([18, 16, 11, 12, 8, 4, -1, -4, -4, -7])
"""
m = np.sum((x - np.mean(x)) * (y - np.mean(y))) / np.sum((x - np.mean(x))**2)
b = np.mean(y) - m * np.mean(x)
lt. Folien eine alternative methode 
"""
xm, ym = x.mean(), y.mean()
m = x.dot(y - ym) / x.dot(x - xm)
b = ym - m * xm
m = x.dot(y - ym) / x.dot(x - xm)
b = ym - m * xm
m = x.dot(y - ym) / x.dot(x - xm)
b = ym - m * xm

print(f"Steigung (m) = {m}, Ordinatenabschnitt (b) = {b}")

# Aufgabe 2
v = np.polyfit(x, y,1)
print(f"{v}")

#Aufgabe 3
y_reg = m * x + b

ss_total = np.sum((y - np.mean(y))**2)
ss_residuen = np.sum((y - y_reg)**2)

r_2 = 1 - (ss_residuen / ss_total)

print(f"R^2 = {r_2}")

#Aufgabe 4
X = np.array([[2,-3,0,0,0],[4,0,5,0,-2],[1,1,1,1,1],[0,3,1,-4,-1],[-4,-2,-3,0,-5]])
Y = np.array([-13,7,1,-1,24]).transpose()

v = np.linalg.inv(X) @ Y
print(v.T)
print(f"a = {v.T[0]}, b = {v.T[1]}, c = {v.T[2]}, d = {v.T[3]}, e = {v.T[4]}")
"""
im fstring werden die ergebnisse als folat ausgegeben da np diese bei der ausgabe in int umwandelt 
print(f"a = {int(v.T[0])}, b = {int(v.T[1])}, c = {int(v.T[2])}, d = {int(v.T[3])}, e = {int(v.T[4])}")
#pythonmachtspaß
"""
