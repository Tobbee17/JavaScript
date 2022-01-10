navn= str(input("Skriv inn en tekst: "))

siffer = 0

for k in navn:
    if k.isdigit():
        siffer += 1
print("Antall siffer er: ", siffer)