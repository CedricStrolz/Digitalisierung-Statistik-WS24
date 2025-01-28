# Aufgabe 13.1
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import stats, f_oneway

df = pd.read_excel("Testdaten-Freitag.xlsx", sheet_name=0)

n0 = df['Normal-T0'].dropna()
n1 = df['Normal-T1'].dropna()
e0 = df['Erhoeht-T0'].dropna()
e1 = df['Erhoeht-T1'].dropna()

plt.hist(n0, bins=10, alpha=0.5, label="Normal-T0")
plt.hist(e0, bins=10, alpha=0.5, label="Erhoeht-T0")
plt.xlabel("Triglyceridkonzentration (in mg / dl)")
plt.ylabel("Anzahl der Personen")
plt.legend()
plt.show()

plt.hist(n1, bins=10, alpha=0.5, label="Normal-T1")
plt.hist(e1, bins=10, alpha=0.5, label="Erhoeht-T1")
plt.xlabel("Triglyceridkonzentration (in mg / dl)")
plt.ylabel("Anzahl der Personen")
plt.legend()
plt.show()

def signifikanz(p):
    if p <= 0.001:
        return "hoch signifikant"
    elif p <= 0.01:
        return "sehr signifikant"
    elif p <= 0.05:
        return "signifikant"
    else:
        return "nicht signifikant"
    
t_stat, p_value_t0 = stats.ttest_ind(n0, e0, equal_var=True)

print(f"T-Test p-Wert für T0: {p_value_t0}")
print("Signifikanz: ",signifikanz(p_value_t0))

t_stat_erhoeht, p_value_erhoeht = stats.ttest_rel(e0, e1)

print(f"T-Test p-Wert für die Kohorte mit erhöhten Triglyceriden: {p_value_erhoeht}")
print("Signifikanz:", signifikanz(p_value_erhoeht))

# Aufgabe 13.2
df = pd.read_excel("Testdaten-Freitag.xlsx", sheet_name=1)

ass = df['ASS Kopczynski'].dropna()
para = df['Paracetadur Forte'].dropna()
ibu = df['Ibuprofi 5000mg'].dropna()

f_stat, p_value = f_oneway(ass, para, ibu)

print(f"ANOVA p-Wert: {p_value}")
print("Signifikanz:", signifikanz(p_value))