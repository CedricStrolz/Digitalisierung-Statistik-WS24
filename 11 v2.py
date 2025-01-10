import pandas as pd
from scipy.stats import linregress, pearsonr        #mehrere Bibliotheken möglich aber scipy wird auf stackoverflow empfohlen
#import matplotlib

regressiondata = pd.read_excel(r'/home/cedrics/Downloads/Daten-Mittwoch.ods', sheet_name='Regression', engine='odf')   #"engine='odf' => einlesen von ods dateien ist NUR automatisch bei Pandas(ab Version 0.25) dabei wenn odspy installiert ist

x = regressiondata['x']
y = regressiondata['y']

slope, intercept, r_value, p_value, std_err = linregress(x, y)

pearson_corr = pearsonr(x, y)

results_t1 = f"Steigung = {slope}, Ordinatenabschnitt = {intercept}, R² = {r_value}, Standardabweichung = {std_err}"

#print(matplotlib.pyplot.scatter(x,y))  wollte noch einen scatterplot der Daten hinzufügen hatte aber leider keine zeit :(
print(results_t1)

inventardata = pd.read_excel(r'/home/cedrics/Downloads/Daten-Mittwoch.ods', sheet_name='Inventar', engine='odf')

print(inventardata.groupby(['Kategorie']).sum())
print(inventardata.groupby(['Kategorie']).max())            #wäre für solchen operationen nich SQL besser geigent (besonders bei großen Datnmengen)?