#!/usr/bin/env python3
# Bearbeitung vom 6. Übungsblatt in Digitalisierung und Statistik


# 6.1
print("Hello World!")


# 6.2
s = (2, 1)
e = (4, 5)

m = (e[1] - s[1]) / (e[0] - s[0])
b = s[1] - m * s[0]

print(f"Durch die Punkte S = {s} und E = {e} verläuft die Gerade "
      f"y={int(m) if m.is_integer() else m}*x "
      f"{'-' if b < 0 else '+'} "
      f"{abs(int(b)) if b.is_integer() else (abs(b))}")


# 6.3
string_1 = "Digitalisierung und Statistik"[3::2]
string_2 = "dreh mal am herd"[::-1]
string_3 = "Heute arbeitete er am Computer etwas länger".replace("er", "sie")

print(f"{string_1}\n{string_2}\n{string_3}")


# 6.4
def ostersonntag(_jahreszahl: int):
    J = _jahreszahl

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
        print(f"Der Ostersonntag im Jahr {J} ist am {OS - 31}. April!")
    else:
        print(f"Der Ostersonntag im Jahr {J} ist am {OS}. März!")


# Jahreszahlen von denen das Datum des Ostersonntags berechnet werden soll
jahreszahlen = [1980, 2000, 2020]
for jahreszahl in jahreszahlen:
    ostersonntag(jahreszahl)
