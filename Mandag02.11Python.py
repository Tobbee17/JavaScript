Brukskonto = float(input("Hva er balansen på brukskontoen din?: "))
Sparekonto = float(input("Hva er balansen på sparekontoen din?: "))

Velgkonto=(input("Hvilken konto vil du velge? brukskonto eller sparekonto: "))

if "bruks" in Velgkonto:
    Bruks=str(input("Du valgte Brukskonto. Vil du sette inn eller ta ut penger?: "))
    if "inn" in Bruks:
        penger=float(input("Hvor mye vil du sette inn?: "))
        Brukskonto = Brukskonto + penger
        print("Ny balanse er: ", Brukskonto, "Kr")
    elif "ut" in Bruks:
        penger=float(input("Hvor mye penger vil du ta ut?: "))
        Brukskonto = Brukskonto - penger
        print("Ny balanse er: ", Brukskonto, "Kr")

    elif "spare" in Velgkonto:
            Sparebalanse=str(input("Du valgte sparekonto. Vil du ta ut eller sette inn penger?: "))
    if "inn" in Sparebalanse:
        penger=float(input("Hvor mye penger vil du sette inn?: "))
        Sparekonto = Sparekonto + penger
    print("Ny balanse er: ", Sparekonto, "Kr")
    
    elif "ut" in Sparebalanse:
        
        