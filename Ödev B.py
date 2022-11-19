for i in range(0, 101):
    if len(str(i)) == 1:
        i = "0"+str(i)
    if (str(i)[0]) < (str(i)[1]):
        # buradaki if son sayıdan sonraki virgülü almamak için
        if i == 89:
            print(i)
            break
        print(i, end=", ")