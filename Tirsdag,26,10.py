BensinTank = float(input("Skriv inn størrelsen på tanken: "))
BensinForbruk = float(input("Skriv inn bensin forbruk pr mil: "))
Pris = float(input("Skriv inn bensin prisen pr liter: "))
Lengde = float(input("Skriv inn hvor langt du skal kjøre: "))

AntallLiter = Lengde * BensinForbruk
PrisForReise = Pris * AntallLiter
DrivstoffIgjen = BensinTank - AntallLiter

print(PrisForReise)
print(DrivstoffIgjen)