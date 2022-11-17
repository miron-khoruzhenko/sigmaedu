result = ""
x = 0
while(x < 100):
    birler = x%10
    onlar = x//10
    if(birler > onlar):
        if(x < 10):
            result += "0" + str(x) + ", "
        else:
            result += str(x) + ", "
    x += 1
print(result[:len(result) - 2])    