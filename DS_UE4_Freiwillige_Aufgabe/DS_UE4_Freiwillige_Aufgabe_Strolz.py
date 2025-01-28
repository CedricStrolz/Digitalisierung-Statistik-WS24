from numpy import *
from matplotlib import pyplot as plt
import pandas as pd
import scipy.stats as stats




#Aufgabe 1

data_BlutdruckModelle = pd.read_excel(r"/home/cedrics/Downloads/Erhobene-Daten.ods", sheet_name="Bluckdruck-Modelle", engine = 'odf')

XDias_Blutdruckmodelle = data_BlutdruckModelle['x-Dias.']
YDias_Blutdruckmodelle = data_BlutdruckModelle['N(x)-Dias.']
XSys_Blutdruckmodelle = data_BlutdruckModelle['x-Sys.']
YSys_Blutdruckmodelle = data_BlutdruckModelle['N(x)-Sys.']


norm_XDias = linspace(XDias_Blutdruckmodelle.min(), XDias_Blutdruckmodelle.max(), 500)
norm_XSys = linspace(XSys_Blutdruckmodelle.min(), XSys_Blutdruckmodelle.max(), 500)

dfDias = stats.norm.pdf(norm_XDias, loc=XDias_Blutdruckmodelle.mean(), scale=XDias_Blutdruckmodelle.std())
dfSys = stats.norm.pdf(norm_XSys, loc=XSys_Blutdruckmodelle.mean(), scale=XSys_Blutdruckmodelle.std())


fig, ax = plt.subplots(1,2,figsize = (10,5),sharey = True)

ax[0].plot(linspace(XDias_Blutdruckmodelle.min(), XDias_Blutdruckmodelle.max(), 500), dfDias, color = 'fuchsia')
ax[0].set_title("Diastolischer Blutdruck")
ax[0].set_xlabel("x-Dias.")
ax[0].set_ylabel("N(x)-Dias.")
ax[0].grid()

ax[1].plot(linspace(XSys_Blutdruckmodelle.min(), XSys_Blutdruckmodelle.max(),500),dfSys,color = 'fuchsia')
ax[1].set_title("Systolischer Blutdruck")
ax[1].set_xlabel("x-Sys.")
ax[1].set_ylabel("N(x)-Sys.")
ax[1].grid()
plt.show()
plt.close()

#Aufgabe 2

data_Blutdruck = pd.read_excel(r"/home/cedrics/Downloads/Erhobene-Daten.ods", sheet_name="Blutdruck", engine = 'odf')

Dias = data_Blutdruck['Dias. Blutdruck']
Sys = data_Blutdruck['Sys. Blutdruck']

plt.hist(Dias, bins=10, alpha=0.5, label='Dias. Blutdruck', density=True, color='deepskyblue')
plt.hist(Sys, bins=10, alpha=0.5, label='Sys. Blutdruck', density=True, color='orchid')

plt.xlabel("Blutdruck [mmHg]")
plt.ylabel("Häufigkeit")
plt.grid()
plt.legend()
plt.show()
plt.close()

#Aufgabe 3

Blutdruck = [Dias, Sys]
lables = ['Dias. Blutdruck', 'Sys. Blutdruck']
colors = ['mediumseagreen', 'orchid']

fig, ax = plt.subplots()
bplot = ax.boxplot(Blutdruck, patch_artist=True, tick_labels=lables)
for patch, color in zip(bplot['boxes'], colors):
    patch.set_facecolor(color)
plt.ylabel('Blutdruck [mmHg]')
plt.show()
plt.close()

#Aufgabe 4

data_InsulinExperiment = pd.read_excel(r"/home/cedrics/Downloads/Erhobene-Daten.ods", sheet_name="Insulin-Experiment", engine = 'odf')

plasma_data = data_InsulinExperiment[data_InsulinExperiment['Probenursprung'] == 'Plasma']
urin_data = data_InsulinExperiment[data_InsulinExperiment['Probenursprung'] == 'Urin']

plasma_stats = plasma_data.groupby('Tageszeit')['Insulinwert'].agg(['mean', 'std'])
urin_stats = urin_data.groupby('Tageszeit')['Insulinwert'].agg(['mean', 'std'])
categories = ['Morgens', 'Mittags', 'Abends']
x = arange(len(categories))
width = 0.35
fig, ax = plt.subplots(figsize=(10, 6))

ax.bar(x - width/2, plasma_stats['mean'], width, yerr=plasma_stats['std'], label='Plasma',capsize=5, color='skyblue', edgecolor='black')
ax.bar(x + width/2, urin_stats['mean'], width, yerr=urin_stats['std'], label='Urin',capsize=5, color='orange', edgecolor='black')
ax.set_xticks(x)
ax.set_xticklabels(categories)
ax.set_xlabel('Tageszeit')
ax.set_ylabel('Insulinspiegel [pmol/L]')
ax.set_title('Vergleich der Insulinspiegel in Plasma und Urin')
ax.legend()
plt.tight_layout()
plt.show()
