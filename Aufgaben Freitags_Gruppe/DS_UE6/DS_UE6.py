# Aufgabe 6.1
print("Hello World!")

# Aufgabe 6.2
m = (1-5) / (2-4)
b = 1 - m * 2

print("m = ",m,sep='')
print("b = ",b,sep='')

# Aufgabe 6.3
x = "Digitalisierung und Statistik"
x_mod = x[3::2]
print(x_mod)

y = "dreh mal am herd"
y_mod = y[15::-1]
print(y_mod)

z = "Heute arbeitete er am Computer etwas länger."
z_mod = z.replace("er", "sie")
print(z_mod)

# Aufgabe 6.4
def Ostersonntag(J):
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
        print("Der Ostersonntag im Jahr, ",J," ist am ",OS-31,". April",sep='')
    else:
        print("Der Ostersonntag im Jahr, ",J," ist am ",OS,". März",sep='')
    
Ostersonntag(1980)
Ostersonntag(2000)
Ostersonntag(2020)