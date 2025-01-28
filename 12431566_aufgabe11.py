import pandas as pd
import numpy as np
from math import sqrt


# Aufgabe 1

df = pd.read_excel("datenblaetter/Daten-Freitag_11.xlsx", "Regression")

x = np.squeeze(df.loc[:, ["x"]].to_numpy())
y = np.squeeze(df.loc[:, ["y"]].to_numpy())
m, b = np.polyfit(x,y,1)

x_abweichung = x - x.mean()
y_abweichung = y - y.mean()
pearson = x_abweichung.dot(y_abweichung) / (sqrt(x_abweichung.dot(x_abweichung)) * sqrt(y_abweichung.dot(y_abweichung)))

bestimmungsmass = pow(pearson, 2)

print(f"m = {m}\nb = {b}\nBestimmungsmaß = {bestimmungsmass}\nPerson-Koeffizient = {pearson}")

# Aufgabe 2

df = pd.read_excel("datenblaetter/Daten-Freitag_11.xlsx", "Inventar")

vorhandene_artikel = df[["Kategorie", "Anzahl"]].groupby(["Kategorie"]).sum()
print(vorhandene_artikel)

guenstigste_artikel = df[["Kategorie", "Einzelpreis"]].groupby(["Kategorie"]).min()
print(guenstigste_artikel)
