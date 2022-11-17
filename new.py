a = float(input("girdi: "))
list = []
x = 0
z = 1
while z < a:
    list.append(x)
    if x < 1:
        x+=1
    elif x == 1:
        list.append(x)
        x += 1
    else:
        x +=x
    z +=1

print(list)

