# firebit er variabelen som tar in 4 bit
fireBit=input ("Skriv inn et 4-bits tall: ")

# tiTall er variabelen som holder verdien til tallet i 10tallsystemet, og er satt til e
tiTall = 0

# variabelen Leng gir Lengden til firebitstallet
leng=len(fireBit)

# variabel counter er en tellevariabel
# den brukes for å vite hvor Langt man har kommet i firebitstalLlet
counter = 0

# for-Løkken itererer gjennom hver "karakter" (tall) i input-string
# siden k er en string, må vi gjøre om k til integer for å sjekke om den har verdi 1
# det gjøres ved å caste: int(k)
for k in fireBit:
    if counter == 0 and int(k) == 1:      # sjekker om første bit (fra venstre) er 1
        tiTall = tiTall + 128
    elif counter == 1 and int(k) == 1:          
        tiTall = tiTall + 64 
    elif counter == 2 and int(k) == 1:          
        tiTall = tiTall + 32 
    elif counter == 3 and int(k) == 1:         
        tiTall = tiTall + 16                              
    elif counter == 4 and int(k) == 1:         
        tiTall = tiTall + 8             
    elif counter == 5 and int(k) == 1:  
        tiTall = tiTall + 4             
    elif counter == 6 and int(k) == 1:    
        tiTall = tiTall + 2
    elif counter == 7 and int(k) == 1:          
        tiTall = tiTall + 1   
    else:         
        pass
    counter = counter + 1

# printer feridg svar
print ("de 4 bitene ", fireBit, "har verdi ", tiTall, "i 10tallsystemet" )