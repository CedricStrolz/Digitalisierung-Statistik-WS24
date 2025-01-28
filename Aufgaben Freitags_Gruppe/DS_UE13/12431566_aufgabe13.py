#!/usr/bin/env python

from scipy import stats
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

DATENBLATT = "datenblaetter/Testdaten-Freitag_13.xlsx"

# Aufgabe 1

df = pd.read_excel(DATENBLATT, "Triglyceride")
t0_norm = df["Normal-T0"]
t0_erh = df["Erhoeht-T0"].dropna()
t1_norm = df["Normal-T1"]
t1_erh = df["Erhoeht-T1"].dropna()

_, (ax1, ax2) = plt.subplots(1,2,figsize=(12,6))

ax1.hist(t0_norm, label="Normal", alpha=0.5, color="blue")
ax1.hist(t0_erh, label="Erhöht", alpha=0.5, color="orange")
ax1.set_title("T0")

ax2.hist(t1_norm, label="Normal", alpha=0.5, color="blue")
ax2.hist(t1_erh, label="Erhöht", alpha=0.5, color="orange")
ax2.set_title("T1")

xticks = np.arange(100, 210, 10)
ax1.set_xticks(xticks)
ax2.set_xticks(xticks)

yticks = np.arange(0, 10, 1)
ax1.set_yticks(yticks)
ax2.set_yticks(yticks)

ax1.legend()
ax2.legend()
plt.show()


# Aufgabe 2

def signifikanz(n: float) -> str:
    if n <= 0.001:
        return "hoch signifikant"
    elif n <= 0.01:
        return "sehr signifikant"
    elif n <= 0.05:
        return "signifikant"
    return "nicht signifikant"


# Aufgabe 3

_, p_value = stats.ttest_ind(t0_norm, t0_erh)
print(p_value, signifikanz(p_value))

# Aufgabe 4
_, p_value = stats.ttest_rel(t0_erh, t1_erh)
print(p_value, signifikanz(p_value))

# Aufgabe 5

_, p_value = stats.ttest_rel(t0_norm, t1_norm)
print(p_value, signifikanz(p_value))
print("-> leider nicht :(")

# Aufgabe 6

df = pd.read_excel(DATENBLATT, "Wirkdauer")
med1 = df["ASS Kopczynski"].dropna()
med2 = df["Paracetadur Forte"].dropna()
med3 = df["Ibuprofi 5000mg"]

_, p_value = stats.f_oneway(med1, med2, med3)
print(p_value, signifikanz(p_value))
