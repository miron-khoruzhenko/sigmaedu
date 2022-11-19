numbers = []
for i in range(100):
    for j in range(100):
        if i%10>i//10 and  j%10>j//10 and j>i:
            numbers.append("{} {}".format(str(i).zfill(2), str(j).zfill(2)))

print(", ".join(numbers))
