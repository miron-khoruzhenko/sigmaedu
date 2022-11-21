a = b = 0
list = []

while a < 10 and b < 10:
    
    if b > a:
        list.append(str(a)+str(b))
        
        b+=1
        if b == 10:
            b = 0
            a += 1
    else:
        b += 1

print(", ".join(list))