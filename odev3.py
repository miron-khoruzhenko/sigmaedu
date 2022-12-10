import time

f = open("data.txt","w")
f.writelines(["\nName: Al", "\nSurname: Pacino", "\nGender: Male", "\nUsername: Tony Montana", "\nJob: dirty business"])
f.close()
time.sleep(1)

a = open("data.txt","r")
liste = (a.read().split("\n"))
liste.pop(0)
dictinoray = {}
for i in liste:
    b = i.split(": ")
    dictinoray.update({b[0]: b[1]})

print(dictinoray)