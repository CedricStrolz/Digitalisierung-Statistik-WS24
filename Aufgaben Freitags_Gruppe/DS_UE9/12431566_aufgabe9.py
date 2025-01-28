#!/usr/bin/env python
from math import comb, pow


# Aufgabe 1
def ist_palindrom(s: str) -> bool:
    for i in range(0, len(s) // 2):
        if s[i] != s[-i - 1]:
            return False
    return True


print(f"otto ist {'ein' if ist_palindrom('otto') else 'kein'} Palindrom")
print(f"affe ist {'ein' if ist_palindrom('affe') else 'ein'} Palindrom")
print(f"radar ist {'ein' if ist_palindrom('radar') else 'kein'} Palindrom")


# Aufgabe 2 & 3

def binom(k: int, p: float, n: int) -> float:
    res = comb(n, k) * pow(p, k) * pow(1 - p, n - k)
    print(f"Die Wahrscheinlichkeit für die Werte k = {k}, p = {p} und n = {n} ist: {res}")
    return res


binom(0, 0.011, 42)
binom(3, 0.1666, 5)
binom(6, 0.5, 15)


# Aufgabe 4

for s in "12/24/2024".split("/"):
    print(s)
