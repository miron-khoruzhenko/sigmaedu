

for i in range(1,100):
    if(i<10):
       print("0"+ str(i),end=", ")
    else:
     a = i//10
     b = i%10
     if(i==89):
        print(i)
     else:
        if(b>a):
           print(str(i),end=", ")
            
        