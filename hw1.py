numbers = []
for i in range(100):
    if i%10>i//10:
        numbers.append(str(i).zfill(2))

print(", ".join(numbers))
#print(*numbers, sep=", ") #also works
