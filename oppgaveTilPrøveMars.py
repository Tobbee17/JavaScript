sentinel=input()

while sentinel !="Q":
    x= float(input("Skriv in en bølgelengde\n")) 
    lysetshastighet = 300000000
    frekvens = lysetshastighet / x
    if x > 0:
        print("bølgelengden har en frekvens på", frekvens)
        break