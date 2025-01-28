import pandas as pd
import numpy as np
from scipy.stats import linregress, norm
import matplotlib.pyplot as plt


regression_data = pd.read_excel(r'/home/cedrics/Documents/Messdaten-Mittwoch.ods', sheet_name='Regression', engine='odf')
wirkdauer_data = pd.read_excel(r'/home/cedrics/Documents/Messdaten-Mittwoch.ods', sheet_name='Wirkdauer', engine='odf')

x = regression_data['x']
y = regression_data['y']

slope, intercept, r_value, p_value, std_err = linregress(x, y)

y_reg = slope * x + intercept
round_solpe = round(slope, 4)
round_intercep = round(intercept, 4)

plt.scatter(x, y, label="Gemessene Punkte", color="blue", lw = 1)
plt.plot(x,y_reg, label=f"{round_solpe} * x + {round_intercep}; R² = {round(r_value, 4)}", color="red", lw = 2)

plt.title("Lineare Regression der Messdaten")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()
plt.close()

a = wirkdauer_data['ASS Kopczynski']
b = wirkdauer_data['Paracetadur Forte']
c = wirkdauer_data['Ibuprofi 5000mg']

'''
rangea = list(range(a.min(),a.max()))
rangeb = list(range(b.min(),b.max()))
rangec = list(range(c.min().c.max()))
'''

x_range = np.linspace(min(a.min(), b.min(), c.min()), max(a.max(), b.max(), c.max()), 500) #asu mir unerfindlichen gründen hat die erste variante nicht funktionirt und ich musste auf stackoverflow zurückgreifen (warscheinlich kann der range befel nicht mit floats arbeiten)

anorm = norm.pdf(x_range, a.mean(), a.std())
bnorm = norm.pdf(x_range, b.mean(), b.std())
cnorm = norm.pdf(x_range, c.mean(), c.std())

plt.hist(a, bins=10, alpha=0.5, label='ASS Kopczynski', density=True, color='deepskyblue')
plt.hist(b, bins=10, alpha=0.5, label='Paracetadur Forte', density=True, color ='fuchsia')
plt.hist(c, bins=10, alpha=0.5, label='Ibuprofi 5000mg', density=True, color='mediumseagreen')

plt.plot(x_range, anorm, color='cornflowerblue')
plt.plot(x_range, bnorm, color='orchid')
plt.plot(x_range, cnorm, color='seagreen')


plt.title("Histogramm Wirkdauer")
plt.legend()
plt.xlabel("Wirkdauer [min]")
plt.ylabel("Anzahl")
plt.show()
plt.close()
