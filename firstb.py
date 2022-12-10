for i in range(0, 101):
    if len(str(i)) == 1:
        i = "0"+str(i)
    if (str(i))[0] < (str(i))[1]:
        if i == 89:
            print(i)
            break
        print(i,end=", ")
    



for x in range(10):
    for y in range(10):
        if y > x:
            print("{0}{1}".format(x, y), end=", ")