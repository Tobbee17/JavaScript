navn= str(input("Skriv inn en tekst: "))

k = ""
vokalene = "aeiouyæøåAEIOUYÆØÅ"

for letter in navn:
    if letter in vokalene:
        k += '_'
    else:
       k += letter

print(k)