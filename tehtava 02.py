
luvut = []

while True:
        syote = input("Anna luku (tyhjä lopettaa): ")
        if syote == "":
            break
        luku = int(syote)
        luvut.append(luku)
reverse=True
luvut.sort(reverse=True)
print("Viisi suurinta lukua:")

for i in range(min(5, len(luvut))):
    print(luvut[i])