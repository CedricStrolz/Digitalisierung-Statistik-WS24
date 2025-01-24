print("Hello World!")



x1, y1 = 2, 7
x2, y2 = -3, -8

k = (y2 - y1) / (x2 - x1)

d = y1 - k * x1

print(f"Steigung (k): {k}")
print(f"Ordinatenabschnitt (d): {d}")
print(f"f(x) = {k}*x + {d}")


String = "Digitalisierung und Statistik"
Ausgabe = String[2::3]
print(Ausgabe)


String2 = "vitaler nebel mit sinn ist im leben relativ"
Ausgabe2 = String2[::-1]
print(Ausgabe2)


String3 = "Heute arbeitet er am Comuter etwas länger"
String3.replace("er", "sie")


J = 1984
K = J//100
M = 15+(3*K+3)//4-(8*K+13)//25
S = 2-(3*K+3)//4
A = J%19
D = (19*A+M)%30
R = (D+A//11)//29
OG = 21+D-R
SZ = 7-(J+J//4+S)%7
OE = 7-(OG-SZ)%7
OS = OG+OE
April = "April 1984"
Maerz = "Maerz 1984"
if OS > 31 :
    OSneu = OS -31
    print(OSneu, April)
else:
    print(OS, Maerz)


J = 2004
K = J//100
M = 15+(3*K+3)//4-(8*K+13)//25
S = 2-(3*K+3)//4
A = J%19
D = (19*A+M)%30
R = (D+A//11)//29
OG = 21+D-R
SZ = 7-(J+J//4+S)%7
OE = 7-(OG-SZ)%7
OS = OG+OE
April = "April 2004"
Maerz = "Maerz 2004"
if OS > 31 :
    OSneu = OS -31
    print(OSneu, April)
else:
    print(OS, Maerz)


# In[47]:


J = 2024
K = J//100
M = 15+(3*K+3)//4-(8*K+13)//25
S = 2-(3*K+3)//4
A = J%19
D = (19*A+M)%30
R = (D+A//11)//29
OG = 21+D-R
SZ = 7-(J+J//4+S)%7
OE = 7-(OG-SZ)%7
OS = OG+OE
April = "April 2024"
Maerz = "Maerz 2024"
if OS > 31 :
    OSneu = OS -31
    print(OSneu, April)
else:
    print(OS, Maerz)
