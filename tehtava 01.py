import random
# Kirjoita ohjelma, joka kysyy käyttäjältä arpakuutioiden lukumäärän.
lukumäärän=int(input("arpakuutioiden lukumäärän"))
summa = 0
for i in range(lukumäärän):
    silmaluku = random.randint(1, 6)
    summa = silmaluku+summa
print(f"Silmälukujen summa on {summa}")


