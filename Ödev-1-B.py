result = ""
for onlar in range(0, 10):
    for birler in range(0,10):
        if birler > onlar:
            result += (str(onlar) + str(birler) + ", ")

print(result[:-2])