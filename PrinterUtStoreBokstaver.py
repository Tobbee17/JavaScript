navn= str(input("Skriv inn en tekst: "))

vokaler = 0

for k in navn:
    if (k == 'A' or k == 'E' or k == 'I' or k == 'O' or k == 'U' or k == 'Y' or k == 'Æ' or k == 'Ø' or k == 'Å' or k == 'a'
       or k == 'e' or k == 'i' or k == 'o' or k == 'u' or k == 'y' or k == 'æ' or k == 'ø' or k == 'å'):
        vokaler += 1
print("Antall vokaler: ", vokaler)