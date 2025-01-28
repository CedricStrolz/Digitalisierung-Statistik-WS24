#!/usr/bin/env python

# Aufgabe 1
s = 0
i = 1
while i <= 12345:
    if i % 2 == 0:
        s += i
    i += 1

print(f"Die Summe aller Zahlen von 1 bis 12345 ist {s}.")


# Aufgabe 2
text = "regallager"
ist_palindrom = True
laenge = len(text)

for i in range(0,laenge//2):
    i_gegen = laenge -1 -i
    if text[i] != text[i_gegen]:
        ist_palindrom = False
        break

print(f"\"{text}\" ist {'ein' if ist_palindrom else 'kein'} Palindrom.")
