# Aufgabe 14.1
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import stats
from statsmodels.stats.multitest import multipletests

df = pd.read_excel("Proteomics-Experiment.xlsx", sheet_name=0)

df = df.dropna(subset=["Treated-1", "Treated-2", "Treated-3", "Treated-4"], how="all")
df = df.dropna(subset=["Control-1", "Control-2", "Control-3"], how="all")

treated_data = df.iloc[:,1:5]
treated_data = treated_data.transpose()
control_data = df.iloc[:,5:]
control_data = control_data.transpose()

tStats, pValues = stats.ttest_ind(treated_data, control_data, nan_policy="omit")
n_signifikant = sum(pValues < 0.05)
print(f"{n_signifikant} Proteine sind statistisch signifikant.")

plt.hist(pValues, bins=50, alpha=0.5, label="pValue")
plt.xlabel("pValue")
plt.ylabel("Häufigkeit")
plt.legend()
plt.show()

pValues_corr = multipletests(pValues, method="fdr_bh")[1]
n_signifikant_corr = sum(pValues_corr < 0.05)
print(f"{n_signifikant_corr} Proteine sind nach korrektur statistisch signifikant.")

plt.hist(pValues_corr, bins=50, alpha=0.5, label="pValue korrigiert")
plt.xlabel("pValue korrigiert")
plt.ylabel("Häufigkeit")
plt.legend()
plt.show()