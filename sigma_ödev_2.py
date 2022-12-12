sayı = int(input("Lütfen Seçtiğiniz Sayıyı Giriniz: "))

if sayı <=1:
    print("2")
    
def asalsayı(sayı):
    
    for i in range(2,sayı+1):
        if sayı%i==0:
            if sayı==i:
                print(sayı)
                break
            else:
                s_asal = sayı+1
                asal_k = True
                
                while True:
                    for i in range(2,s_asal):
                        if s_asal%i ==0:
                            asal_k = False
                        break
                    if asal_k:
                        return s_asal
                    else:
                        s_asal = s_asal+1
                        if s_asal % 2 == 0:
                            s_asal = s_asal+1
                        asal_k = True
            
çalıştır = asalsayı(sayı)

print(çalıştır)

input()
