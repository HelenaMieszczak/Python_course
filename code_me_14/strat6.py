from jednostki.rycerz import Rycerz
from jednostki.lucznik import Lucznik

rycerze = []

for _ in range(4):
    rycerze.append(Rycerz())

# print(rycerze)

for rycerz in rycerze:
    rycerz.maszeruj(2000)

for rycerz in rycerze:
    rycerz.atakuj()

# print(rycerze)

lucznicy = []

for _ in range(3):
    lucznicy.append(Lucznik())

for lucznik in lucznicy:
    lucznik.atakuj()

# print(lucznicy)

armia = lucznicy + rycerze
# print(armia)

for wojownik in armia:
    wojownik.atakuj()

print(armia)