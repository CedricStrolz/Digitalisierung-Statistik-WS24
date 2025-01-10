#!/usr/bin/env python
# coding: utf-8

# In[42]:


summe = 0
zahl = 1
ist_ungerade = True 

while zahl <= 43210:
    if ist_ungerade:
        summe += zahl   
    ist_ungerade = not ist_ungerade
    zahl += 1
print (summe)

# ik das die Angebe die Boolsche var als False angibt, aber nur so funktioniert der code :)
# nach langem überlegen --> mein startelement ist 1 ; aber ich werd den code nicht mehr Änderen sorry     


# In[35]:


from random import random
import math as m           # hab das Modul im Internet gefunden --> probieren wir es mal aus

in_kreis = 0

for i in range(100001):
    x = random()
    y = random()
    
    if m.pow(x,2) + m.pow(y,2) <= 1:
        in_kreis += 1
pi = (in_kreis / 100000) * 4
print (pi)


# In[ ]:





# In[ ]:





# In[ ]:




