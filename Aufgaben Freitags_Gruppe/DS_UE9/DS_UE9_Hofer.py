# Aufgabe 9.1
def Palindrom_check(text):
    ist_palindrom = True
    laenge = len(text)

    for i in range(0,(laenge // 2)):
        i_gegen = -1-i
        if text[i] != text[i_gegen]:
            ist_palindrom = False
            break    

    print(ist_palindrom)
    return ist_palindrom

Palindrom_check("otto")
Palindrom_check("affe")
Palindrom_check("radar")

# Aufgabe 9.2/9.3
import math

def binom(k,p,n):
    B = math.comb(n,k)*(p**k)*(1-p)**(n-k)
    print(f"Die Wahrscheinlichkeit für die Werte k = {k}, p = {p} und n = {n} ist: {B}")
    return B

binom(0,0.011,42)
binom(3,0.1666,5)
binom(6,0.5,15)

# Aufgabe 9.4
Datum = "12/24/2024"
Ausgabe = Datum.split("/")
for i in range(3):
    print(Ausgabe[i])

