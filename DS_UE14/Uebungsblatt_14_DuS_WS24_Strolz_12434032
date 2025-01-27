import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
from statsmodels.stats.multitest import multipletests

data = pd.read_excel(r"/home/cedrics/Downloads/Proteomics-Experiment.ods", sheet_name="Proteins", engine = 'odf')
data = data.dropna(subset = ['Treated-1', 'Treated-2', 'Treated-3' , 'Treated-4'], how = 'all')
data = data.dropna(subset = ['Control-1', 'Control-2', 'Control-3'], how = 'all')


treated = ["Treated-1", "Treated-2", "Treated-3", "Treated-4"]
control = ["Control-1", "Control-2", "Control-3"]
treated_data = data[["Description"] + treated].set_index("Description").T
control_data = data[["Description"] + control].set_index("Description").T

tStats, pVals = stats.ttest_ind(treated_data, control_data, nan_policy = 'omit')
sigpVals = [pval for pval in pVals if pval < 0.05]
print(len(sigpVals))

pValues_corr = multipletests(pVals, method = 'fdr_bh')[1]
sigpVals_corr = [pval for pval in pValues_corr if pval < 0.05]
print(len(sigpVals_corr))

plt.hist(pVals, bins = 100, alpha = 0.75, color = 'fuchsia')
plt.ylabel('Anzhal')
plt.xlabel('p-Value')
plt.grid()
plt.title('Histogram der p-values')
plt.show()
plt.close()

plt.hist(pValues_corr, bins = 100, alpha = 0.75, color = 'mediumseagreen')
plt.ylabel('Anzhal')
plt.xlabel('p-Value')
plt.title('Histogram der korregierten p-values')
plt.grid(True)
plt.show()
plt.close()
