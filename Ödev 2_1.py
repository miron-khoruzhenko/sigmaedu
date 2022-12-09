Sayi =int(input("Bir sayı giriniz : "))

counter = 0

for i in range(2,Sayi):
    if (Sayi % i) == 0:
        counter = counter+1

if (counter==0):
    print(Sayi,"Sayisi Asaldır")
else:
    print(Sayi,"Sayisi Asal Değildir")