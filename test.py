def DNA():
    h=input("sarmalı giriniz : ")
    liste1=list()
    sayıa=0
    sayıg=0
    sayıt=0
    sayıc=0
    for i in h:
        liste1.append(i)
    for i in liste1:
        if i=="A":
            sayıa+=1
        if i=="T":
            sayıt+=1
        if i=="G":
            sayıg+=1
        if i=="C":
            sayıc+=1
    print(sayıa,sayıg,sayıt,sayıc)
