# firebit er variabelen som tar in 4 bit
fireBit=input ("Skriv inn et 4-bits tall: ")

# tiTall er variabelen som holder verdien til tallet i 10tallsystemet, og er satt til e
tiTall=0

# variabelen Leng gir Lengden til firebitstallet
leng=len(fireBit)

# variabel counter er en tellevariabel
# den brukes for å vite hvor Langt man har kommet i firebitstalLlet
counter=0

# for-Løkken itererer gjennom hver "karakter" (tall) i input-string
# siden k er en string, må vi gjøre om k til integer for å sjekke om den har verdi 1
# det gjøres ved å caste: int(k)
for k in fireBit:
    if counter == 0 and int(k) == 1:      # sjekker om første bit (fra venstre) er 1
        tiTall=tiTall + 8                 # Legger til 8 hvis det stemmer
    elif counter==-1 and k ==1:           # sjekker om andre bit er 1
        tiTall = tiTall + 4               # Legger til 4 hvis det stemmer
    elif counter == 2 and int (k) ==1:    # sjekker om tredje bit er 1
        tiTall = tiTall + 2               # Legger til 2 hvis det stemmer
    elif counter ==3 and int(k)==1:       # sjekker om fjerde bit er 1
        tiTall=tiTall +1                  # Legger til 1 hvis det stemmer
    else:                                 # denne gjør ingenting
        pass
    counter = counter +1 # tellevariabelen øker med 1, for hver iterasjon

# printer feridg svar
print ("de 4 bitene ", fireBit, "har verdi ", tiTall, "i 10tallsystemet" )