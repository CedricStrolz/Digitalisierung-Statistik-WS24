#!/usr/bin/env python
# coding: utf-8

# In[8]:


#Aufgabe 1
M2 = {2 * i for i in range(1, 11)}
M3 = {3 * i for i in range(1, 11)}
M4 = {4 * i for i in range(1, 11)} 

print("M2:", M2)
print("M3:", M3)
print("M4:", M4)

nur_M2 = M2 - (M3 | M4)
nur_M3 = M3 - (M2 | M4)
nur_M4 = M4 - (M2 | M3)

print("Nur in M2:", nur_M2)
print("Nur in M3:", nur_M3)
print("Nur in M4:", nur_M4)

M2_M3_ohne_M4 = (M2 & M3) - M4
M3_M4_ohne_M2 = (M3 & M4) - M2
M2_M4_ohne_M3 = (M2 & M4) - M3

print("Schnittmenge von M2 und M3 ohne M4:", M2_M3_ohne_M4)
print("Schnittmenge von M3 und M4 ohne M2:", M3_M4_ohne_M2)
print("Schnittmenge von M2 und M4 ohne M3:", M2_M4_ohne_M3)

In_allen = M2 & M3 & M4
print("In allen drei Mengen:", In_allen)


# In[52]:


# Aufgabe 2
encode_lerzeichen = {chr(32): 0}                # der chr(i) befehl gibt das zeichen mit dem korrospondierendem unicode aus " " = 32
encode_zeichen = {chr(i): i - 64 for i in range(65, 91)}
encode = {}
encode.update(encode_lerzeichen)
encode.update(encode_zeichen)             #zusammenfügen der dictionarys

decode = dict((v, k) for k, v in encode.items())    #invertieren des encode dict zum erstellen des decode --> Stackoverflow 

Nachricht = "PYTHON IST COOL"
Nachricht_Verschlüsselt = list(encode[i] for i in Nachricht)                    #verschlüsseln des Strings aus der angabe

Nachricht2 = [4, 5, 18, 0, 1, 4, 12, 5, 18, 0, 9, 19, 20, 0, 7, 5, 12, 1, 14, 4, 5, 20]
entschlüsseltenachrichrt2 = list(decode[i] for i in Nachricht2)                 #decoden der listen aus der angabe

N2 = "".join(entschlüsseltenachrichrt2)                   #umwandeln der entschlüsselten liste mittels des join befehls in einen string --> danke Stackoverflow

print(encode)
print(decode)
print(Nachricht_Verschlüsselt)
print(entschlüsseltenachrichrt2)
print(N2)
print("in the end we would like to thank our sponsor stackoverflow")


# In[ ]:




