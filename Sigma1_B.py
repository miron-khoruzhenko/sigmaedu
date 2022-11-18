a = b = 0

while a < 10 and b < 10:
    
    if b > a:
        print(str(a)+str(b))
        b+=1
        if b == 10:
            b = 0
            a += 1
    else:
        b += 1