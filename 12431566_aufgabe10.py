#!/usr/bin/env python

import numpy as np
from math import sqrt

# Aufgabe 1

x = np.array(range(1, 10))
y = np.array([-5, -4, -3 - 1, 2, 2, 3, 4, 8, 7])

xm, ym = x.mean(), y.mean()
m = x.dot(y - ym) / x.dot(x - xm)
b = ym - m * xm

print(f"m = {m}; b = {b}")

# Aufgabe 2

v = np.polyfit(x, y, 1)
print(v)

# Aufgabe 3

x_abweichung = x - x.mean()
y_abweichung = y - y.mean()
pearson = x_abweichung.dot(y_abweichung) / (sqrt(x_abweichung.dot(x_abweichung)) * sqrt(y_abweichung.dot(y_abweichung)))
print(pearson)

# Aufgabe 4

x = np.array([[0, 0, 1, 0, 1], [2, -3, 0, 1, 0], [1, 1, 1, 1, 1], [0, -4, 0, 0, -3], [2, -4, 0, 2, -5]])
y = np.array([4, 15, 7, -1, 3]).transpose()

v = np.linalg.inv(x) @ y
print(v.T)
