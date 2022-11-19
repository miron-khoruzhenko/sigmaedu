#for i in range(100): [print("{:02d} {:02d}".format(i, j), end=",") for j in range(100) if i%10>i//10 and  j%10>j//10 and j>i]

#print('.'.join([(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]))
#print(", ".join(['{0:02d}'.format(i) for i in range(100) if i%10>i//10]))

print(', '.join(["{} {}".format(str(i).zfill(2), str(j).zfill(2)) for i in range(100) for j in range(100) if i%10>i//10 and j%10>j//10 and j>i]))
