#Aufgabe 1
def ostern(jahr):
    J = jahr
    K = J // 100
    M = 15 + (3 * K + 3) // 4 - (8 * K + 13) // 25
    S = 2 - (3 * K + 3) // 4
    A = J % 19
    D = (19 * A + M) % 30
    R = (D + A // 11) // 29
    OG = 21 + D - R
    SZ = 7 - (J + J // 4 + S) % 7
    OE = 7 - (OG - SZ) % 7
    OS = OG + OE
    if OS > 31:
        return print(f"{OS - 31}.April.{jahr}")
    else:
        return print(f"{OS}.März.{jahr}")

for jahr in range(2020, 2031):
    ostern(jahr)

#Aufgabe 2
import math as m

def norm(x,mu=0,s=1):
    exponent = m.exp(-(x-mu)**2/(2*s**2))
    vorfaktor = 1/(s*m.sqrt(2*m.pi))
    erg = vorfaktor*exponent
    return erg
print(norm(0))
print(norm(2,1,3))
print(norm(-2,2,8))

#Aufgabe 3
import math as m  # diese zeile ist redundant da math bereits eimeal importiert wurde --> wird aus formalität (neue aufabe) so beibehalten

def norm_erw(x,mu=0,s=1):
    exponent = m.exp(-(x-mu)**2/(2*s**2))
    vorfaktor = 1/(s*m.sqrt(2*m.pi))
    erg = vorfaktor*exponent
    return print(f"Die Warscheinlichkeitsdichte für die werte x={x}, mu={mu}, sigma={s} ist: {erg}")

norm_erw(0)
norm_erw(2,1,3)
norm_erw(-2,2,8)

#Aufgabe 4
string = "21.12.2024"
for i in string.split("."):
    print(i)


