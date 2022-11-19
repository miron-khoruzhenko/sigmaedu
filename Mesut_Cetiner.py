dna=input("Enter the DNA code:")

list1=[]
for ch in dna:
    if ch not in list1:
        list1.append(ch)
        print (dna.count(ch), end=" ")
