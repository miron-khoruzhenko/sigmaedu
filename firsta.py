from random import *
def DNA(a): 
    A = 0
    T = 0
    G = 0
    C = 0
    for harf in str(a):
        if harf == "A" or harf == 'a':      
            A += 1
        elif harf == "T" or harf == 't':      
            T += 1
        elif harf == "G" or harf == 'g':      
            G += 1
        elif harf == "C" or harf == 'c':      
            C  += 1
    print(A ," ", T ," ", G ," ",C)

def sayi_bilgisi(a):
    print({girdi: a.count(girdi) for girdi in a})

def other_sayi_bilgisi(b):
    sonuc = {"A":0,
    "C":0,
    "T":0,
    "G":0 }

    for i in b:
        if i == "A":
            sonuc["A"] = b.count(i)
        if i == "G":
            sonuc["G"] = b.count(i)
        if i == "C":
            sonuc["C"] = b.count(i)
        if i == "T":
            sonuc["T"] = b.count(i)
    print(sonuc)

liste = []
liste2 = []
while randint(0,1000) > len(liste):
    liste.append(randint(0,4))

for i in liste:
    if i == 0:
        liste2.append("A")
    if i == 1:
        liste2.append("T")
    if i == 2:
        liste2.append("G")
    if i == 3:
        liste2.append("C")

DNA(liste2)
sayi_bilgisi(liste2)
other_sayi_bilgisi(liste2)
print(liste2)