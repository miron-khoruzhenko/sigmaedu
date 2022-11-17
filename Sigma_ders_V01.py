# Herhangi bir uzunlukta DNA string girdisi alan Fonksiyon tanımlayın. Bu fonksiyon “A”, “C”,
#“G”, “T” sembollerinin kaç kere yazıldığını gösteren boşlukla ayrılmış 4 tam sayı
#döndürmeli.


# kullanıcıdan DNA girdisi al
# aldığın dizeleri harf harf ayır
# her harfi listeye ekle
#liste içinde gezinerek harflerin neye eşit olduklarını bul
#örnek T==T ise t_sayisi=t_sayisi+1 yap.


#TCAAGGCCGCCTGGGGTAAGGTCGGCGCGCACGCTGGCGAGTATGGTGCGGAGGCCCTGGAGAGGATGTTCCTGTCCTTCCCCACCACCAAGACCTACTTCCCGCACTTCGACCTGAGCCACGGCTCTGCCCAGGTTAAGGGCCACGGCAAGAAGGTGGCCGACGCGCTGACCAACGCCGTGGCGCACGTGGACGACATGCCCAACGCGCTGTCCGCCCTGAGCGACCTGCACGCGCACAAGCTTCGGGTGGACCCGGTCAACTTCAAGCTCCTAAGCCACTGCCTGCTGGTGACCCTGGCCGCCCACCTCCCCGCCGAGTTCACCCCTGCGGTGCACGCCTCCCTGGACAAGTTCCTGGCTTCTGTGAGCACCGTGCTGACCTCCAAATACCGTTAAGCTGGAGCCTCGGTGGCCATGCTT


print("DNA girdisini yazınız: ")

DNA= input()

def DNA_sayici(DNA):
    a_sayac=0
    c_sayac=0
    g_sayac=0
    t_sayac=0
    print("DNA girdisini yazınız: ")
    x=list(DNA)

    harfler=list(DNA)
    print(harfler)

    print("Listenin Uzunluğu: ", len(harfler)) 


    for i in range(len(harfler)):
        if harfler[i]== "A":
            a_sayac= a_sayac+1

    for i in range(len(harfler)):
        if harfler[i]== "C":
            c_sayac= c_sayac+1

    for i in range(len(harfler)):
        if harfler[i]== "G":
            g_sayac= g_sayac+1

    for i in range(len(harfler)):
        if harfler[i]== "T":
            t_sayac= t_sayac+1

            
    print(a_sayac, " ",c_sayac, " ",g_sayac, " ",t_sayac)

DNA_sayici(DNA)






