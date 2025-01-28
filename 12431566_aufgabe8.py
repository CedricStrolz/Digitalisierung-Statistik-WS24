#!/usr/bin/env python
import string

# Aufgabe 1

m4 = set([i * 4 for i in range(1, 11)])
m8 = set([i * 8 for i in range(1, 11)])
m12 = set([i * 12 for i in range(1, 11)])

print(f"Ausschließlich in M4: {m4 - m8 - m12}")
print(f"Ausschließlich in M8: {m8 - m4 - m12}")
print(f"Ausschließlich in M12: {m12 - m4 - m8}")

print(f"Enthalten in M4 und M8. Nicht enthalten in M12: {m4 & m8 - m12}")
print(f"Enthalten in M8 und M12. Nicht enthalten in M4: {m8 & m12 - m4}")
print(f"Enthalten in M4 und M12. Nicht enthalten in M8: {m4 & m12 - m8}")

print(f"Enthalten in M4, M8 und M12: {m4 & m8 & m12}")

# Aufgabe 2
uppercase_letters = string.ascii_uppercase + " "
encode = {uppercase_letters[i]: i for i in range(27)}
decode = {i: uppercase_letters[i] for i in range(27)}


def encode_string(s: str) -> list[int]:
    s = s.upper()
    encoded = []
    for c in s:
        encoded.append(encode[c])
    return encoded


def decode_list(l: list[int]) -> str:
    decoded = ""
    for n in l:
        decoded += decode[n]
    return decoded


print(encode_string("DIGITALISIERUNG UND STATISTIK"))
print(decode_list([3, 0, 18, 26, 15, 0, 10, 4, 19, 26, 8, 18, 19, 26, 0, 13, 6, 4, 10, 14, 12, 12, 4, 13]))
