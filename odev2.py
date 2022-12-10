def asalsayilar():
    a = int(input("bir sayı giriniz: "))
    b = 0
    if a == 2:
        print(a,"asal sayıdır.")
    elif a == 1 or a == 0:
        print(a,"asal sayı değildir.")
    else:
        for i in range(2,a):
            if a % i == 0:
                print(a,"asal sayi değildir.")
                b = 2
                break
            
        if b == 0: 
            print(a,"asal sayıdır.")    


asalsayilar()