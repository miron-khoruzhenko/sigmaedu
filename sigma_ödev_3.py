import json
data = []

#get information

name = input("İsminizi Giriniz: ")
surname = input("Soyisminizi Giriniz: ")
gender = input("Cinsiyetinizi Giriniz: ")
username = input("Kullanıcı Adınızı Giriniz: ")
job = input("İşinizi Giriniz: ")

#set array

data.append({"Name":"{}".format(name),"Surname":"{}".format(surname),"Gender":"{}".format(gender),"Username":"{}".format(username),"Job":"{}".format(job)})

#create file

with open("data.json","w") as dosya:
    json.dump(data,dosya)
    
    
with open("data.json","r") as dosya:
    data = json.load(dosya)

print(data)

input()