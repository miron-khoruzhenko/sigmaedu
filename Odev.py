def asal_mi():
    
    asal = True
    
    istenen = input("Lütfen bir tam sayı giriniz:")

    if istenen.isdigit():
        
        sayi = int(istenen)
        
        if sayi > 2:
           
               for i in range(2, sayi):
               
                   if sayi % i == 0:
                   
                       asal = False
           
               if asal == True:
                
                   print("Sayi Asaldır")
                    
               else:
                        
                   print("Sayi Asal Değildir")
           
        elif sayi == 2:
           
               print("Sayı Asaldır")
           
    
        else:
           
               print("Sayı Asal Değildir")
           
           
    else:
    
        print("Lütfen bir tam sayı giriniz")
        