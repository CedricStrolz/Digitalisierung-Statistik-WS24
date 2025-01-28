summe = 0
zahl = 1
ist_ungerade = True 

while zahl <= 43210:
    if ist_ungerade:
        summe += zahl   
    ist_ungerade = not ist_ungerade
    zahl += 1
print (summe)


from random import random
import math as m           
in_kreis = 0

for i in range(100001):
    x = random()
    y = random()
    
    if m.pow(x,2) + m.pow(y,2) <= 1:
        in_kreis += 1
pi = (in_kreis / 100000) * 4
print (pi)
