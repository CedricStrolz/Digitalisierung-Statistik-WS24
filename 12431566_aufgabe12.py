#!/usr/bin/env python

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from math import sqrt, floor, ceil

# Aufgabe 1

df = pd.read_excel("datenblaetter/Messdaten-Freitag_12.xlsx", "Regression")

x = np.squeeze(df.loc[:, ["x"]].to_numpy())
y = np.squeeze(df.loc[:, ["y"]].to_numpy())
m, b = np.polyfit(x, y, 1)

x_abweichung = x - x.mean()
y_abweichung = y - y.mean()
pearson = x_abweichung.dot(y_abweichung) / (sqrt(x_abweichung.dot(x_abweichung)) * sqrt(y_abweichung.dot(y_abweichung)))

bestimmungsmass = pow(pearson, 2)

plt.scatter(x, y, label="Gemessene Punkte")

x_lin = np.array(range(floor(x.min()), ceil(x.max()) + 1))
y_lin = m * x_lin + b
plt.plot(x_lin, y_lin, label=f"y = {m}x {'+' if b >= 0 else '-'} {abs(b)}, R2 = {bestimmungsmass}", color="orange")

plt.legend()
plt.show()

plt.close()

# Aufgabe 2 & 3

df = pd.read_excel("datenblaetter/Messdaten-Freitag_12.xlsx", "Wirkdauer")

med1 = (df["ASS Kopczynski"], "ASS Kopczynski", "blue")
med2 = (df["Paracetadur Forte"], "Paracetadur Forte", "orange")
med3 = (df["Ibuprofi 5000mg"], "Ibuprofi 5000mg", "red")
meds = [med1, med2, med3]


def normalverteilung(x, m, s):
    return np.exp(-0.5 * ((x - m) / s) ** 2) / (s * np.sqrt(2 * np.pi))


for med in meds:
    mue, sigma = med[0].mean(), med[0].std()
    plt.hist(med[0], label=med[1], alpha=0.5, density=True, color=med[2])
    x = np.array(range(floor(med[0].min()), ceil(med[0].max()) + 1))
    y = normalverteilung(x, mue, sigma)
    plt.plot(x, y, lw=2, color=med[2])

plt.legend()
plt.show()
