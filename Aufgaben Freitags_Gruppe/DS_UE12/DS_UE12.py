# Aufgabe 12.1
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress, norm

df = pd.read_excel("Messdaten-Freitag.xlsx", sheet_name=0)

x = df['x'].values
y = df['y'].values

m, b, r, *_ = linregress(x,y)
r2 = r ** 2

plt.scatter(x,y,label="Gemessene Punkte")
x_fit = np.array([x.min(), x.max()])
y_fit = m * x_fit + b
plt.plot(x_fit, y_fit, color="black", label=f"y = {m:.3} * x + {b:.3}, R2 = {r2:.3}")
plt.legend()
plt.show()

# Aufgabe 12.2
df = pd.read_excel("Messdaten-Freitag.xlsx", sheet_name=1)

for i in df.columns:
    plt.hist(df.dropna()[i], bins=10, alpha=0.5, label=i, density=True)
    mittelwert, std = norm.fit(df.dropna()[i])
    x_min, x_max = plt.xlim()
    x = np.linspace(x_min, x_max, 100)
    p = norm.pdf(x, mittelwert, std)
    plt.plot(x, p, color="black", linewidth=2)
plt.xlabel("Wirkdauer [min]")
plt.ylabel("Anzahl")
plt.legend()
plt.show()