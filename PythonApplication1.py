
for i in range(0,10):
   for j in range(0,10):
       if(j > i):
          if(i == 9 & j == 9):
             print(f'{i}{j}')
          else:
             print(f'{i}{j}',end=', ')
       else:
           continue
   
