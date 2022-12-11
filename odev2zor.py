def cank():
    a = int(input("bir sayı giriniz: "))
    b = 0
    if a == 2:
        print(a)
    elif a == 1 or a == 0:
        print(2)
    else:
        for i in range(2,a):
            if a % i == 0:
                b = 2
                break
            
        if b == 0: 
            print(a)
        elif b == 2:
            
            for c in range(a,1000000):
                counter = 0
                print(c)
                for z in range(2,c):
                    if c % z == 0 :
                        counter =counter+1
                        print(z)
                        print(c)
                        break
                if counter == 0:
                    print(c)
                    break


cank()

