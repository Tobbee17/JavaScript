frekvens=int(eval(input("Skriv inn en frekvens ")))

lyshastighet = 3*10**8

bølgelengde = lyshastighet/frekvens
if bølgelengde > 3*10**3 and bølgelengde < 30*10**3:
    print("frekvensen i båndet er 3 kHz -> 30 kHz (VLF)")
elif bølgelengde > 3*10*4 and bølgelengde < 3*10*5:
    print("frekvensen i båndet er 30 kHz -> 300 kHz (LF)")
elif bølgelengde > 3*10*5 and bølgelengde < 3*10*6:
    print("frekvensen i båndet er 300 kHz -> 3 MHz (MF)")
elif bølgelengde > 3*10*6 and bølgelengde < 3*10*7:
    print("frekvensen i båndet er 3 MHz -> 30 MHz (HF)")
elif bølgelengde > 3*10*7 and bølgelengde < 3*10*8:
    print("frekvensen i båndet er 30 MHz -> 300 MHz (VHF)")
elif bølgelengde > 3*10*8 and bølgelengde < 3*10*9:
    print("frekvensen i båndet er 300 MHz -> 3 GHz (UHF)")
elif bølgelengde > 3*10*9 and bølgelengde < 3*10*10:
    print("frekvensen i båndet er 3 GHz -> 30 GHz (SHF)")
elif bølgelengde > 3*10*10 and bølgelengde < 3*10*11:
    print("frekvensen i båndet er 30 GHz -> 300 GHz (EHF)")