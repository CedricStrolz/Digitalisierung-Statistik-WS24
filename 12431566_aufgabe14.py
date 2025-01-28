#!/usr/bin/env python

import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
from statsmodels.stats.multitest import multipletests

DATENBLATT = "datenblaetter/Proteomics-Experiment_14.xlsx"

# Aufgabe 1

df = pd.read_excel(DATENBLATT)
treated = ["Treated-1", "Treated-2", "Treated-3", "Treated-4"]
control = ["Control-1", "Control-2", "Control-3"]

df = df.dropna(subset=treated, how="all")
df = df.dropna(subset=control, how="all")

# Aufgabe 2

df_treated = df.loc[:, treated].transpose()
df_control = df.loc[:, control].transpose()

# Aufgabe 3

_, pValues = stats.ttest_ind(df_treated, df_control, nan_policy="omit")
signifikant = [pValue for pValue in pValues if pValue < 0.05]
print(f"Anzahl statisch signifikanter Proteine (alpha < 0.05): {len(signifikant)}")

# Aufgabe 4

plt.hist(pValues, bins=50)
plt.xlabel("p-Values")
plt.ylabel("Häufigkeit")
plt.show()

# Aufgabe 5

pValues_corr = multipletests(pValues, method="fdr_bh")[1]
signifikant_corr = [pValue_corr for pValue_corr in pValues_corr if pValue_corr < 0.05]
print(f"Anzahl statisch signifikanter Proteine (alpha < 0.05) nach Korrektur: {len(signifikant_corr)}")


# Aufgabe 6

plt.close()

plt.hist(pValues_corr, bins=50)
plt.xlabel("Korrigierte p-Values")
plt.ylabel("Häufigkeit")
plt.show()

