for i in range(1,11): #Ytre for-løkke: bestemmer antall løkker
    for j in range(1,11): # Indre for-løkke: bestemme antall kolonner
        print(i*j, end=" ")
    print()

from random import random, randint #metodene fra random-modul må importeres

kast=randint(1,6) #gir ett tilfeldig heltall(integer) mellom 1 og 6 
kast2=randint(1,6) #gir ett tilfeldig heltall(integer) mellom 1 og 6 
for i in range(1,11): #Ytre løkke
    print("Kast",i,"ble:",kast,"og",kast2) 
    for j in range(2): #indre løkke 
        print() # tom print-funksjon for å starte ny linje etter indre for-løkke.

