balansen = float(input("Skriv inn balansen på kontoen din: "))

penger = str(input("Skriv in Innskudd for å sette inn penger og Utak for å ta ut penger: "))

if "Inn" in penger:
    Innskudd=float(input("Skriv inn hvor mye penger du vil sette inn: "))
    InnskuddBalanse = Innskudd + balansen
    print("Ny balanse er: ", InnskuddBalanse, "Kr")

elif "Ut" in penger:
    Utak=float(input("Hvor mye penger vil du ta ut? "))
    UtakBalanse = balansen - Utak
    print("Ny balanse er: ", UtakBalanse, "Kr")