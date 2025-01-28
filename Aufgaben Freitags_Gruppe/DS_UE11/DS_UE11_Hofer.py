# Aufgabe 11.1
import numpy as np
import pandas as pd

from sklearn.metrics import r2_score
from scipy.stats import pearsonr

df = pd.read_excel("Daten-Freitag.xlsx", sheet_name=0)
df.head()

x = df['x'].values
y = df['y'].values

m,b = np.polyfit(x,y,1)
print(f"m ist: {m} und b ist: {b}")

f = m * x + b
r2 = r2_score(y,f)
print(f"r2 ist {r2}")

r_x_y, _ = pearsonr(x,y)
print(f"Der Pearson Korrelationskoeffizient beträgt {r_x_y}")

# Aufgabe 11.2
df = pd.read_excel("Daten-Freitag.xlsx", sheet_name=1)

tabelle1 = df.groupby('Kategorie')['Anzahl'].sum().reset_index()
print(f"Summe aller vorhandener Artikel:\n{tabelle1}")

tabelle2 = df.groupby('Kategorie')['Einzelpreis'].min().reset_index()
print(f"Preis des günstigsten Artikles:\n{tabelle2}")