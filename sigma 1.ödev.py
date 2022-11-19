import random

elemanlar = ("A","T","G","C")
DNA = [] 
for i in range(1000):
    
    DNA.append(elemanlar[random.randint(0,3)])

DNA2 = []

for i in elemanlar:
    count = 0
    for j in DNA:
        
        if i == j:
            
            count += 1
    DNA2.append(count)

metin = ""

for i in DNA:
    
    metin = metin + i

print(metin,"\n")

print("""{}'dan {} tane var
{}'den {} tane var
{}'den {} tane var
{}'den {} tane var""".format(elemanlar[0],DNA2[0],elemanlar[1],DNA2[1],elemanlar[2],DNA2[2],elemanlar[3],DNA2[3]))

input()