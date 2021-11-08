Brukskonto = float(input("Hva er balansen på brukskontoen din?: "))
Sparekonto = float(input("Hva er balansen på sparekontoen din?: "))

Velgkonto=(input("Hvilken konto vil du velge? brukskonto eller sparekonto: "))

if "bruks" in Velgkonto:
    Bruks=str(input("Du valgte Brukskonto. Vil du sette inn eller ta ut penger?: "))
    if "inn" in Bruks:
        penger=float(input("Hvor mye vil du sette inn?: "))
        Brukskonto = Brukskonto + penger
        
    elif "ut" in Bruks:
        penger=float(input("Hvor mye penger vil du ta ut?: "))
        Brukskonto = Brukskonto - penger

if "spare" in Velgkonto:
    Spare=str(input("Du valgte sparekonto. Vil du ta ut eller sette inn penger?: "))
    if "inn" in Spare:
        penger=float(input("Hvor mye penger vil du sette inn?: "))
        Sparekonto = Sparekonto + penger
    
    elif "ut" in Spare:
        penger=float(input("Hvor mye penger vil du ta ut?"))
        Sparekonto = Sparekonto - penger
        
print("Total brukskonto balanse er:" , Brukskonto, "Kr")
print("Total sparekonto balanse er:" , Sparekonto, "Kr")