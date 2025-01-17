# Aufgabe 10.1
import numpy as np

x = np.array([1,2,3,4,5,6,7,8,9,10])
y = np.array([-5,-4,-3,-1,2,2,3,4,8,7])

xm, ym = x.mean(), y.mean()
m = x.dot(y - ym) / x.dot(x - xm)
b = ym - m * xm
print(f"m ist: {m} und b ist: {b}.")

# Aufgabe 10.2
v = np.polyfit(x,y,1)
print(f"v ist: {v}")

# Aufgabe 10.3
f = m * x + b
r_x_y =np.sqrt(1 - np.var(f - y) / np.var(y))
print(f"Der Pearson Korrelationskoeffizient beträgt: {r_x_y}")

# Aufgabe 10.4
X = np.array([[0,0,1,0,1], [2,-3,0,1,0], [1,1,1,1,1], [0,-4,0,0,-3], [2,-4,0,2,-5]])
Y = np.array([4,15,7,-1,3]).transpose()
v = np.linalg.inv(X) @ Y
print(f"Die Lösungen für a, b, c, d und e betragen: {v.T}")