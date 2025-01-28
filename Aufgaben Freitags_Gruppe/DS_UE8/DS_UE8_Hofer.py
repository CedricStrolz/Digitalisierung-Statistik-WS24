# Aufgabe 8.1
set_1 = {4,8,12,16,20,24,28,32,36,40}
set_2 = {8,16,24,32,40,48,56,64,72,80}
set_3 = {12,24,36,48,60,72,84,96,108,120}

set_1_only = set_1.difference(set_2,set_3)
print("Nur in Set 1 enthalten:",set_1_only)
set_2_only = set_2.difference(set_1,set_3)
print("Nur in Set 2 enthalten:",set_2_only)
set_3_only = set_3.difference(set_1,set_2)
print("Nur in Set 3 enthalten:",set_3_only)

set_1_2 = set_1.intersection(set_2)
set_1_2 = set_1_2.difference(set_3)
print("In Set 1 und 2 enthalten aber nicht in Set 3:",set_1_2)

set_2_3 = set_2.intersection(set_3)
set_2_3 = set_2_3.difference(set_1)
print("In Set 2 und 3 enthalten aber nicht in Set 1:",set_2_3)

set_1_3 = set_1.intersection(set_3)
set_1_3 = set_1_3.difference(set_2)
print("In Set 1 und 3 enthalten aber nicht in Set 2:",set_1_3)

set_1_2_3 = set_1.intersection(set_2,set_3)
print("In allen Sets enthalten:",set_1_2_3)

# Aufgabe 8.2
encode = {chr(i + 65): i for i in range(26)}
encode[" "] = 26

decode = {value: key for key, value in encode.items()}

message = "DIGITALISIERUNG UND STATISTIK"
encoded = []

for i in message:
    encoded.append(encode[i])

print(encoded)

encoded_message = [3, 0, 18, 26, 15, 0, 10, 4, 19, 26, 8, 18, 19, 26, 0, 13, 6, 4, 10, 14, 12, 12, 4, 13]
decoded = []

for i in encoded_message:
    decoded.append(decode[i])
    
decoded_message = "".join(decoded)
print(decoded_message)