# Aufgabe 7.1
i = 1
summe = 0

while i <= 12345:
    if i % 2 == 0:
        summe += i
    i += 1
        
print(summe)

# Aufgabe 7.2
text = "regallager"
ist_palindrom = True
laenge = len(text)

for i in range(0,(laenge // 2)):
    i_gegen = -1-i
    if text[i] != text[i_gegen]:
        ist_palindrom = False
        break
        
print(ist_palindrom)