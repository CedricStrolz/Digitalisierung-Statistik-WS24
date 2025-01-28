import pandas as pd
import scipy.stats as stats
from matplotlib import pyplot as plt

data_cholesterol = pd.read_excel(r"/home/cedrics/Downloads/Testdaten-Mittwoch.ods", sheet_name="Cholesterol", engine = 'odf')
data_painm = pd.read_excel(r"/home/cedrics/Downloads/Testdaten-Mittwoch.ods", sheet_name="Wirkdauer", engine = 'odf')

data_cholesterol = data_cholesterol.dropna()
data_pain = data_painm.dropna()

normal_T0 = data_cholesterol["Normal-T0"]
normal_T1 =data_cholesterol["Normal-T1"]
erhoeht_T0 =data_cholesterol["Erhoeht-T0"]
erhoeht_T1 =data_cholesterol["Erhoeht-T1"]

fig, ax = plt.subplots(1,2,figsize = (10,5),sharey = True)

ax[0].hist(normal_T0, bins=10, alpha=0.5, label='Normal-T0', density=True, color='deepskyblue')
ax[0].hist(erhoeht_T0, bins=10, alpha=0.5, label='Erhoeht-T0', density=True, color='fuchsia')
ax[0].set_title("Cholesterol - T0")
ax[0].set_xlabel("Cholesterol")
ax[0].set_ylabel("Density")
ax[0].grid()
ax[0].legend()

ax[1].hist(normal_T1, bins=10, alpha=0.5, label='Normal-T1', density=True, color='deepskyblue')
ax[1].hist(erhoeht_T1, bins=10, alpha=0.5, label='Erhoeht-T1', density=True, color='fuchsia')
ax[1].set_title("Cholesterol - T1")
ax[1].set_xlabel("Cholesterol")
ax[1].legend()
ax[1].grid()
plt.show()
plt.close()

def signifikanz(p):
    if p <= 0.0001:
        return "hoch signifikant"

    if p <= 0.01:
        return "sehr signifikant"

    if p <= 0.05:
        return "signifikant"

    else:
        return "nicht signifikant"

t_stat_T0, p_value_T0 = stats.ttest_ind(normal_T0, erhoeht_T0, equal_var = False, nan_policy = "omit")
t_stat_T1, p_value_T1 = stats.ttest_ind(erhoeht_T0, erhoeht_T1, equal_var = True, nan_policy = "omit")

signifikanz_T0 = signifikanz(t_stat_T0)
signifikanz_T1 = signifikanz(t_stat_T1)  # warum wird hier ein nicht signifikant ausgegebnen 10^-25 sit doch ganz klar kleiner als 0.001???

print(f"t-Test der 2 Kohorten bei T0, p = {p_value_T0} => {signifikanz_T0} | t-Test der Kohorten mit erhoehtem Colesterolspiegem bei T0 & T1, p = {p_value_T1} => {signifikanz_T1}")

t_stat_med, p_value_med = stats.ttest_rel(erhoeht_T0, erhoeht_T1)
signifikanz_med = signifikanz(p_value_med)
print(f"gebpaarter t-Test der Kohorte erhoeht, p = {p_value_med} => {signifikanz_med}")



a = data_painm['ASS Kopczynski']
b = data_painm['Paracetadur Forte']
c = data_painm['Ibuprofi 5000mg']

f_stat, p_value_anova = stats.f_oneway(a, b, c, nan_policy='omit')
signifikanz_anova = signifikanz(p_value_anova)
print(f"ANOVA Test der 3 Unterschiedlichen Medikamente, p = {p_value_anova}  => {signifikanz_anova}")
