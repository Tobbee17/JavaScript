from random import randint

sentinel=input("skriv Q for å avslutte, eller hvilken som helst tast for å kaste ")
while sentinel !="Q":
    kast1=randint(1,6)
    kast2=randint(1,6)

    if kast1==kast2:
        print(kast1, kast2, "Du fikk to like!!", )
    else:
        print("Du fikk ", kast1, " og ", kast2)
    sentinel=input("skriv Q for å avslutte, eller hvilken som helst tast for å kaste ")